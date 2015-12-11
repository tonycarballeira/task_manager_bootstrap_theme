from django.shortcuts import render

from django.core import serializers

from main_tables.models import *

 

# Create your views here.
def home(request):
	account = "Modules"
	context = {
		"template_title": account,
		"data": SysSyaAccount.objects.filter(sya_id=7)[0].sys_sym_modules.all()
	}
	return render(request, "home.html", context)