from django import template

register = template.Library()

from main_tables.models import *


@register.simple_tag
def my_modules(value):

	arr = []
	query = SysSyaAccount.objects.filter(sya_id=value)[0].sys_sym_modules.all()
	
	for x in query:
		arr.append(x.sym_name)
	return arr