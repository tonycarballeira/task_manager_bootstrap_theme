from __future__ import absolute_import, unicode_literals

try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

import django
from django.db.models.sql import compiler
import re

NEEDS_AGGREGATES_FIX = django.VERSION[:2] < (1, 7)

# query_class returns the base class to use for Django queries.
# The custom 'SqlServerQuery' class derives from django.db.models.sql.query.Query
# which is passed in as "QueryClass" by Django itself.
#
# SqlServerQuery overrides:
# ...insert queries to add "SET IDENTITY_INSERT" if needed.
# ...select queries to emulate LIMIT/OFFSET for sliced queries.

# Pattern to scan a column data type string and split the data type from any
# constraints or other included parts of a column definition. Based upon
# <column_definition> from http://msdn.microsoft.com/en-us/library/ms174979.aspx
_re_data_type_terminator = re.compile(
    r'\s*\b(?:' +
    r'filestream|collate|sparse|not|null|constraint|default|identity|rowguidcol' +
    r'|primary|unique|clustered|nonclustered|with|on|foreign|references|check' +
    ')',
    re.IGNORECASE,
)


class SQLCompiler(compiler.SQLCompiler):
    def resolve_columns(self, row, fields=()):
        values = []
        index_extra_select = len(self.query.extra_select)
        for value, field in zip_longest(row[index_extra_select:], fields):
            # print '\tfield=%s\tvalue=%s' % (repr(field), repr(value))
            if field:
                try:
                    value = self.connection.ops.convert_values(value, field)
                except ValueError:
                    pass
            values.append(value)
        return row[:index_extra_select] + tuple(values)

    def compile(self, node):
        """
        Added with Django 1.7 as a mechanism to evalute expressions
        """
        sql_function = getattr(node, 'sql_function', None)
        if sql_function and sql_function in self.connection.ops._sql_function_overrides:
            sql_function, sql_template = self.connection.ops._sql_function_overrides[sql_function]
            if sql_function:
                node.sql_function = sql_function
            if sql_template:
                node.sql_template = sql_template
        return super(SQLCompiler, self).compile(node)

    def _fix_aggregates(self):
        """
        MSSQL doesn't match the behavior of the other backends on a few of
        the aggregate functions; different return type behavior, different
        function names, etc.

        MSSQL's implementation of AVG maintains datatype without proding. To
        match behavior of other django backends, it needs to not drop remainders.
        E.g. AVG([1, 2]) needs to yield 1.5, not 1
        """
        for alias, aggregate in self.query.aggregate_select.items():
            sql_function = getattr(aggregate, 'sql_function', None)
            if not sql_function or sql_function not in self.connection.ops._sql_function_overrides:
                continue
            sql_function, sql_template = self.connection.ops._sql_function_overrides[sql_function]
            if sql_function:
                self.query.aggregate_select[alias].sql_function = sql_function
            if sql_template:
                self.query.aggregate_select[alias].sql_template = sql_template

    def as_sql(self, with_limits=True, with_col_aliases=False):
        # Django #12192 - Don't execute any DB query when QS slicing results in limit 0
        if with_limits and self.query.low_mark == self.query.high_mark:
            return '', ()

        if NEEDS_AGGREGATES_FIX:
            # Django 1.7+ provides SQLCompiler.compile as a hook
            self._fix_aggregates()

        # Get out of the way if we're not a select query or there's no limiting involved.
        has_limit_offset = with_limits and (self.query.low_mark or self.query.high_mark is not None)
        try:
            if not has_limit_offset:
                # The ORDER BY clause is invalid in views, inline functions,
                # derived tables, subqueries, and common table expressions,
                # unless TOP or FOR XML is also specified.
                setattr(self.query, '_mssql_ordering_not_allowed', with_col_aliases)

            # let the base do its thing, but we'll handle limit/offset
            sql, fields = super(SQLCompiler, self).as_sql(
                with_limits=False,
                with_col_aliases=with_col_aliases,
            )

            if has_limit_offset:
                if ' order by ' not in sql.lower():
                    # Must have an ORDER BY to slice using OFFSET/FETCH. If
                    # there is none, use the first column, which is typically a
                    # PK
                    sql += ' ORDER BY 1'
                sql += ' OFFSET %d ROWS' % (self.query.low_mark or 0)
                if self.query.high_mark is not None:
                    sql += ' FETCH NEXT %d ROWS ONLY' % (self.query.high_mark - self.query.low_mark)
        finally:
            if not has_limit_offset:
                # remove in case query is ever reused
                delattr(self.query, '_mssql_ordering_not_allowed')

        return sql, fields

    def get_ordering(self):
        # The ORDER BY clause is invalid in views, inline functions,
        # derived tables, subqueries, and common table expressions,
        # unless TOP or FOR XML is also specified.
        if getattr(self.query, '_mssql_ordering_not_allowed', False):
            if django.VERSION[1] == 1 and django.VERSION[2] < 6:
                return (None, [])
            return (None, [], [])
        return super(SQLCompiler, self).get_ordering()


class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler):
    # search for after table/column list
    _re_values_sub = re.compile(
        r'(?P<prefix>\)|\])(?P<default>\s*|\s*default\s*)values(?P<suffix>\s*|\s+\()?',
        re.IGNORECASE
    )
    # ... and insert the OUTPUT clause between it and the values list (or DEFAULT VALUES).
    _values_repl = r'\g<prefix> OUTPUT INSERTED.{col} INTO @sqlserver_ado_return_id\g<default>VALUES\g<suffix>'

    def as_sql(self, *args, **kwargs):
        # Fix for Django ticket #14019
        if not hasattr(self, 'return_id'):
            self.return_id = False

        result = super(SQLInsertCompiler, self).as_sql(*args, **kwargs)
        if isinstance(result, list):
            # Django 1.4 wraps return in list
            return [self._fix_insert(x[0], x[1]) for x in result]

        sql, params = result
        return self._fix_insert(sql, params)

    def _fix_insert(self, sql, params):
        """
        Wrap the passed SQL with IDENTITY_INSERT statements and apply
        other necessary fixes.
        """
        meta = self.query.get_meta()

        if meta.has_auto_field:
            if hasattr(self.query, 'fields'):
                # django 1.4 replaced columns with fields
                fields = self.query.fields
                auto_field = meta.auto_field
            else:
                # < django 1.4
                fields = self.query.columns
                auto_field = meta.auto_field.db_column or meta.auto_field.column

            auto_in_fields = auto_field in fields

            quoted_table = self.connection.ops.quote_name(meta.db_table)
            if not fields or (auto_in_fields and len(fields) == 1 and not params):
                # convert format when inserting only the primary key without
                # specifying a value
                sql = 'INSERT INTO {0} DEFAULT VALUES'.format(
                    quoted_table
                )
                params = []
            elif auto_in_fields:
                # wrap with identity insert
                sql = 'SET IDENTITY_INSERT {table} ON;{sql};SET IDENTITY_INSERT {table} OFF'.format(
                    table=quoted_table,
                    sql=sql,
                )

        # mangle SQL to return ID from insert
        # http://msdn.microsoft.com/en-us/library/ms177564.aspx
        if self.return_id and self.connection.features.can_return_id_from_insert:
            col = self.connection.ops.quote_name(meta.pk.db_column or meta.pk.get_attname())

            # Determine datatype for use with the table variable that will return the inserted ID
            pk_db_type = _re_data_type_terminator.split(meta.pk.db_type(self.connection))[0]

            # NOCOUNT ON to prevent additional trigger/stored proc related resultsets
            sql = 'SET NOCOUNT ON;{declare_table_var};{sql};{select_return_id}'.format(
                sql=sql,
                declare_table_var="DECLARE @sqlserver_ado_return_id table ({col_name} {pk_type})".format(
                    col_name=col,
                    pk_type=pk_db_type,
                ),
                select_return_id="SELECT * FROM @sqlserver_ado_return_id",
            )

            output = self._values_repl.format(col=col)
            sql = self._re_values_sub.sub(output, sql)

        return sql, params


class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):
    pass


class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):
    def as_sql(self):
        sql, params = super(SQLUpdateCompiler, self).as_sql()
        if sql:
            # Need the NOCOUNT OFF so UPDATE returns a count, instead of -1
            sql = 'SET NOCOUNT OFF; {0}; SET NOCOUNT ON'.format(sql)
        return sql, params


class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler):
    def as_sql(self, qn=None):
        self._fix_aggregates()
        return super(SQLAggregateCompiler, self).as_sql(qn=qn)


class SQLDateCompiler(compiler.SQLDateCompiler, SQLCompiler):
    pass

try:
    class SQLDateTimeCompiler(compiler.SQLDateTimeCompiler, SQLCompiler):
        pass
except AttributeError:
    pass
