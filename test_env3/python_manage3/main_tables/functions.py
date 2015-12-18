def run_query(query, *args):

	from django.db import connection

	cursor = connection.cursor()
	sql_query = cursor.execute(query, args)
	records = sql_query.fetchall()

	results = {
		'rows': records,
		'length': len(records)
	}

	return results