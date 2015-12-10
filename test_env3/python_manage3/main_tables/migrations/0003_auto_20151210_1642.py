# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_tables', '0002_auto_20151210_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysrlnsyasym',
            name='rln_sya',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_tables.SysSyaAccount'),
        ),
        migrations.AddField(
            model_name='sysrlnsyasym',
            name='rln_sym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_tables.SysSymModule'),
        ),
        migrations.AddField(
            model_name='syssyaaccount',
            name='sys_sym_modules',
            field=models.ManyToManyField(through='main_tables.SysRlnSyaSym', to='main_tables.SysSymModule'),
        ),
    ]
