from django.shortcuts import render, render_to_response, RequestContext

from django.http import HttpResponseRedirect

from django.core import serializers

from main_tables.models import *

from .forms import SysSyaAccountForm

import Cookie

from django.db import connection

 

# Create your views here.
def home(request):
	
	account = "Modules"
	context = {
		"template_title": account,
		"data": SysSyaAccount.objects.filter(sya_id=7)[0].sys_sym_modules.all()
	}
	return render(request, "home.html", context)

def sign_in(request):
	if request.method == "POST":
		u_name = request.POST.get("sya_name")
		u_password = request.POST.get("sya_password")
		cursor = connection.cursor()
		form = SysSyaAccountForm(initial={"sya_name":"%(u_name)s" % { "u_name":u_name}, "sya_password":"%(u_password)s" % {"u_password":u_password} })
		#using raw sql
		sql_query = cursor.execute("SELECT * FROM  sys_sya_account WHERE sya_name=%s AND sya_password=%s", (u_name, u_password,)) 
		rows = sql_query.fetchall()
		rows_length = len(rows)
		#using orm
		# query = SysSyaAccount.objects.filter(sya_name="%(u_name)s" % {"u_name":u_name}).filter(sya_password="%(u_password)s" % {"u_password":u_password})
		# length = len(query)

		if rows_length > 0:
			response = HttpResponseRedirect("sign_in", locals())
			response.set_cookie("new_cook", "signed_in", max_age = 50000)
			return response

		else:
			error = "User not found"
			return render_to_response("signin.html",	 
  											locals(), 
  											context_instance=RequestContext(request))
	
	else:
		form = SysSyaAccountForm()
		return render_to_response("signin.html",								 
								   locals(), 
								   context_instance=RequestContext(request))






