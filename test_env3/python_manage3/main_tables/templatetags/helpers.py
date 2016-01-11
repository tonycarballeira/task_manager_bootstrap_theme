from django import template

register = template.Library()

from main_tables.models import *


@register.simple_tag
def my_modules(value):

	modules = SysSyaAccount.objects.filter(sya_id=value)[0].sys_sym_modules.all()

	return modules

@register.simple_tag
def my_group(value):

	group = SysSyaAccount.objects.filter(sya_id=value)[0].sys_sym_modules.filter(sym_sym_id = None)

	return group

@register.simple_tag
def sub_groups(value):

	modules = SysSyaAccount.objects.filter(sya_id=value)[0].sys_sym_modules.all()

	group = SysSyaAccount.objects.filter(sya_id=value)[0].sys_sym_modules.filter(sym_sym_id = None)

	sub_groups = SysSyaAccount.objects.filter(sya_id=value)[0].sys_sym_modules.filter(sym_folder = None).exclude(sym_sym_id = None)

	return sub_groups