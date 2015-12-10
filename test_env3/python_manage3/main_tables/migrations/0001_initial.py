# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchemaMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.TextField()),
            ],
            options={
                'db_table': 'schema_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysOstObjectStatus',
            fields=[
                ('ost_id', models.AutoField(serialize=False, primary_key=True)),
                ('ost_name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_ost_object_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRlnSyaSym',
            fields=[
                ('rln_sym_action_add', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_advanced', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_archive', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_delete', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_download', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_edit', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_run', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_test', models.IntegerField(null=True, blank=True)),
                ('rln_sym_action_view', models.IntegerField(null=True, blank=True)),
                ('rln_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'sys_rln_sya_sym',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSlaLogAction',
            fields=[
                ('sla_id', models.AutoField(serialize=False, primary_key=True)),
                ('sla_name', models.CharField(max_length=255, null=True, blank=True)),
                ('sla_sya_id', models.IntegerField(null=True, blank=True)),
                ('sla_sym_id', models.IntegerField(null=True, blank=True)),
                ('sla_ste_id', models.IntegerField(null=True, blank=True)),
                ('sla_action', models.CharField(max_length=50, null=True, blank=True)),
                ('sla_object', models.CharField(max_length=255, null=True, blank=True)),
                ('sla_object_table', models.CharField(max_length=255, null=True, blank=True)),
                ('sla_object_id', models.IntegerField(null=True, blank=True)),
                ('sla_object_ref', models.CharField(max_length=255, null=True, blank=True)),
                ('sla_ip', models.CharField(max_length=50, null=True, blank=True)),
                ('sla_datestamp', models.DateTimeField(null=True, blank=True)),
                ('sla_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_sla_log_action',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSleLogError',
            fields=[
                ('sle_id', models.AutoField(serialize=False, primary_key=True)),
                ('sle_name', models.CharField(max_length=255, null=True, blank=True)),
                ('sle_sya_id', models.IntegerField(null=True, blank=True)),
                ('sle_sym_id', models.IntegerField(null=True, blank=True)),
                ('sle_ste_id', models.IntegerField(null=True, blank=True)),
                ('sle_error_id', models.CharField(max_length=50, null=True, blank=True)),
                ('sle_error_type', models.CharField(max_length=100, null=True, blank=True)),
                ('sle_error_message', models.TextField(null=True, blank=True)),
                ('sle_error_detail', models.TextField(null=True, blank=True)),
                ('sle_error_query', models.TextField(null=True, blank=True)),
                ('sle_url', models.CharField(max_length=255, null=True, blank=True)),
                ('sle_ip', models.CharField(max_length=50, null=True, blank=True)),
                ('sle_datestamp', models.DateTimeField(null=True, blank=True)),
                ('sle_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_sle_log_error',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSlsLogSecurity',
            fields=[
                ('sls_id', models.AutoField(serialize=False, primary_key=True)),
                ('sls_name', models.CharField(max_length=255, null=True, blank=True)),
                ('sls_sya_id', models.IntegerField(null=True, blank=True)),
                ('sls_sym_id', models.IntegerField(null=True, blank=True)),
                ('sls_ste_id', models.IntegerField(null=True, blank=True)),
                ('sls_event', models.CharField(max_length=100, null=True, blank=True)),
                ('sls_url', models.CharField(max_length=255, null=True, blank=True)),
                ('sls_client', models.TextField(null=True, blank=True)),
                ('sls_ip', models.CharField(max_length=50, null=True, blank=True)),
                ('sls_datestamp', models.DateTimeField(null=True, blank=True)),
                ('sls_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_sls_log_security',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSqcQueryControl',
            fields=[
                ('sqc_id', models.AutoField(serialize=False, primary_key=True)),
                ('sqc_sya_id', models.IntegerField(null=True, blank=True)),
                ('sqc_name', models.CharField(max_length=100, null=True, blank=True)),
                ('sqc_column', models.IntegerField(null=True, blank=True)),
                ('sqc_direction', models.CharField(max_length=50, null=True, blank=True)),
                ('sqc_count', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_sqc_query_control',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSteSite',
            fields=[
                ('ste_id', models.AutoField(serialize=False, primary_key=True)),
                ('ste_name', models.CharField(max_length=255, null=True, blank=True)),
                ('ste_value', models.CharField(max_length=255, null=True, blank=True)),
                ('ste_priority', models.IntegerField(null=True, blank=True)),
                ('ste_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_ste_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysStxTextLabel',
            fields=[
                ('stx_id', models.AutoField(serialize=False, primary_key=True)),
                ('stx_name', models.CharField(max_length=100, null=True, blank=True)),
                ('stx_value', models.CharField(max_length=255, null=True, blank=True)),
                ('stx_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_stx_text_label',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSyaAccount',
            fields=[
                ('sya_id', models.AutoField(serialize=False, primary_key=True)),
                ('sya_name', models.CharField(max_length=100, null=True, blank=True)),
                ('sya_email', models.CharField(max_length=100, null=True, blank=True)),
                ('sya_password', models.CharField(max_length=50, null=True, blank=True)),
                ('sya_system', models.IntegerField(null=True, blank=True)),
                ('sya_ste_id', models.IntegerField(null=True, blank=True)),
                ('sya_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_sya_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSymModule',
            fields=[
                ('sym_id', models.AutoField(serialize=False, primary_key=True)),
                ('sym_name', models.CharField(max_length=50, null=True, blank=True)),
                ('sym_icon', models.CharField(max_length=100, null=True, blank=True)),
                ('sym_folder', models.CharField(max_length=100, null=True, blank=True)),
                ('sym_object', models.CharField(max_length=100, null=True, blank=True)),
                ('sym_sym_id', models.IntegerField(null=True, blank=True)),
                ('sym_url', models.CharField(max_length=255, null=True, blank=True)),
                ('sym_priority', models.IntegerField(null=True, blank=True)),
                ('sym_action_add', models.IntegerField(null=True, blank=True)),
                ('sym_action_advanced', models.IntegerField(null=True, blank=True)),
                ('sym_action_archive', models.IntegerField(null=True, blank=True)),
                ('sym_action_delete', models.IntegerField(null=True, blank=True)),
                ('sym_action_download', models.IntegerField(null=True, blank=True)),
                ('sym_action_edit', models.IntegerField(null=True, blank=True)),
                ('sym_action_run', models.IntegerField(null=True, blank=True)),
                ('sym_action_test', models.IntegerField(null=True, blank=True)),
                ('sym_action_view', models.IntegerField(null=True, blank=True)),
                ('sym_beta_date', models.DateTimeField(null=True, blank=True)),
                ('sym_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_sym_module',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSywWhitelist',
            fields=[
                ('syw_id', models.AutoField(serialize=False, primary_key=True)),
                ('syw_name', models.CharField(max_length=255, null=True, blank=True)),
                ('syw_value', models.CharField(max_length=50, null=True, blank=True)),
                ('syw_ste_id', models.IntegerField(null=True, blank=True)),
                ('syw_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sys_syw_whitelist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TstDmoDemo',
            fields=[
                ('dmo_id', models.AutoField(serialize=False, primary_key=True)),
                ('dmo_name', models.CharField(max_length=50, null=True, blank=True)),
                ('dmo_value', models.TextField(null=True, blank=True)),
                ('dmo_price', models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)),
                ('dmo_datestamp', models.DateTimeField(null=True, blank=True)),
                ('dmo_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tst_dmo_demo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TstExpExample',
            fields=[
                ('exp_id', models.AutoField(serialize=False, primary_key=True)),
                ('exp_name', models.CharField(max_length=50, null=True, blank=True)),
                ('exp_value', models.TextField(null=True, blank=True)),
                ('exp_price', models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)),
                ('exp_priority', models.IntegerField(null=True, blank=True)),
                ('exp_ip', models.CharField(max_length=50, null=True, blank=True)),
                ('exp_datestamp', models.DateTimeField(null=True, blank=True)),
                ('exp_ost_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tst_exp_example',
                'managed': False,
            },
        ),
    ]
