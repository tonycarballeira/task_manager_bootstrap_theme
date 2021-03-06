# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 19:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('ost_id', models.AutoField(primary_key=True, serialize=False)),
                ('ost_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sys_ost_object_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSlaLogAction',
            fields=[
                ('sla_id', models.AutoField(primary_key=True, serialize=False)),
                ('sla_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sla_sya_id', models.IntegerField(blank=True, null=True)),
                ('sla_sym_id', models.IntegerField(blank=True, null=True)),
                ('sla_ste_id', models.IntegerField(blank=True, null=True)),
                ('sla_action', models.CharField(blank=True, max_length=50, null=True)),
                ('sla_object', models.CharField(blank=True, max_length=255, null=True)),
                ('sla_object_table', models.CharField(blank=True, max_length=255, null=True)),
                ('sla_object_id', models.IntegerField(blank=True, null=True)),
                ('sla_object_ref', models.CharField(blank=True, max_length=255, null=True)),
                ('sla_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('sla_datestamp', models.DateTimeField(blank=True, null=True)),
                ('sla_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_sla_log_action',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSleLogError',
            fields=[
                ('sle_id', models.AutoField(primary_key=True, serialize=False)),
                ('sle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sle_sya_id', models.IntegerField(blank=True, null=True)),
                ('sle_sym_id', models.IntegerField(blank=True, null=True)),
                ('sle_ste_id', models.IntegerField(blank=True, null=True)),
                ('sle_error_id', models.CharField(blank=True, max_length=50, null=True)),
                ('sle_error_type', models.CharField(blank=True, max_length=100, null=True)),
                ('sle_error_message', models.TextField(blank=True, null=True)),
                ('sle_error_detail', models.TextField(blank=True, null=True)),
                ('sle_error_query', models.TextField(blank=True, null=True)),
                ('sle_url', models.CharField(blank=True, max_length=255, null=True)),
                ('sle_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('sle_datestamp', models.DateTimeField(blank=True, null=True)),
                ('sle_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_sle_log_error',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSlsLogSecurity',
            fields=[
                ('sls_id', models.AutoField(primary_key=True, serialize=False)),
                ('sls_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sls_sya_id', models.IntegerField(blank=True, null=True)),
                ('sls_sym_id', models.IntegerField(blank=True, null=True)),
                ('sls_ste_id', models.IntegerField(blank=True, null=True)),
                ('sls_event', models.CharField(blank=True, max_length=100, null=True)),
                ('sls_url', models.CharField(blank=True, max_length=255, null=True)),
                ('sls_client', models.TextField(blank=True, null=True)),
                ('sls_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('sls_datestamp', models.DateTimeField(blank=True, null=True)),
                ('sls_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_sls_log_security',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSqcQueryControl',
            fields=[
                ('sqc_id', models.AutoField(primary_key=True, serialize=False)),
                ('sqc_sya_id', models.IntegerField(blank=True, null=True)),
                ('sqc_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sqc_column', models.IntegerField(blank=True, null=True)),
                ('sqc_direction', models.CharField(blank=True, max_length=50, null=True)),
                ('sqc_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_sqc_query_control',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSteSite',
            fields=[
                ('ste_id', models.AutoField(primary_key=True, serialize=False)),
                ('ste_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ste_value', models.CharField(blank=True, max_length=255, null=True)),
                ('ste_priority', models.IntegerField(blank=True, null=True)),
                ('ste_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_ste_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysStxTextLabel',
            fields=[
                ('stx_id', models.AutoField(primary_key=True, serialize=False)),
                ('stx_name', models.CharField(blank=True, max_length=100, null=True)),
                ('stx_value', models.CharField(blank=True, max_length=255, null=True)),
                ('stx_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_stx_text_label',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSywWhitelist',
            fields=[
                ('syw_id', models.AutoField(primary_key=True, serialize=False)),
                ('syw_name', models.CharField(blank=True, max_length=255, null=True)),
                ('syw_value', models.CharField(blank=True, max_length=50, null=True)),
                ('syw_ste_id', models.IntegerField(blank=True, null=True)),
                ('syw_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_syw_whitelist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TstDmoDemo',
            fields=[
                ('dmo_id', models.AutoField(primary_key=True, serialize=False)),
                ('dmo_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dmo_value', models.TextField(blank=True, null=True)),
                ('dmo_price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('dmo_datestamp', models.DateTimeField(blank=True, null=True)),
                ('dmo_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tst_dmo_demo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TstExpExample',
            fields=[
                ('exp_id', models.AutoField(primary_key=True, serialize=False)),
                ('exp_name', models.CharField(blank=True, max_length=50, null=True)),
                ('exp_value', models.TextField(blank=True, null=True)),
                ('exp_price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('exp_priority', models.IntegerField(blank=True, null=True)),
                ('exp_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('exp_datestamp', models.DateTimeField(blank=True, null=True)),
                ('exp_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tst_exp_example',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSyaAccount',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('sya_id', models.AutoField(primary_key=True, serialize=False)),
                ('sya_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sya_email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('sya_password', models.CharField(blank=True, max_length=50, null=True)),
                ('sya_system', models.IntegerField(blank=True, null=True)),
                ('sya_ste_id', models.IntegerField(blank=True, null=True)),
                ('sya_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_sya_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRlnSyaSym',
            fields=[
                ('rln_sym_action_add', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_advanced', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_archive', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_delete', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_download', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_edit', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_run', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_test', models.IntegerField(blank=True, null=True)),
                ('rln_sym_action_view', models.IntegerField(blank=True, null=True)),
                ('rln_id', models.AutoField(primary_key=True, serialize=False)),
                ('rln_sya', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sys_rln_sya_sym',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysSymModule',
            fields=[
                ('sym_id', models.AutoField(primary_key=True, serialize=False)),
                ('sym_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sym_icon', models.CharField(blank=True, max_length=100, null=True)),
                ('sym_folder', models.CharField(blank=True, max_length=100, null=True)),
                ('sym_object', models.CharField(blank=True, max_length=100, null=True)),
                ('sym_sym_id', models.IntegerField(blank=True, null=True)),
                ('sym_url', models.CharField(blank=True, max_length=255, null=True)),
                ('sym_priority', models.IntegerField(blank=True, null=True)),
                ('sym_action_add', models.IntegerField(blank=True, null=True)),
                ('sym_action_advanced', models.IntegerField(blank=True, null=True)),
                ('sym_action_archive', models.IntegerField(blank=True, null=True)),
                ('sym_action_delete', models.IntegerField(blank=True, null=True)),
                ('sym_action_download', models.IntegerField(blank=True, null=True)),
                ('sym_action_edit', models.IntegerField(blank=True, null=True)),
                ('sym_action_run', models.IntegerField(blank=True, null=True)),
                ('sym_action_test', models.IntegerField(blank=True, null=True)),
                ('sym_action_view', models.IntegerField(blank=True, null=True)),
                ('sym_beta_date', models.DateTimeField(blank=True, null=True)),
                ('sym_ost_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_sym_module',
                'managed': False,
            },
        ),
    ]
