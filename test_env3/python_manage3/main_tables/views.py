from django.shortcuts import render, render_to_response, RequestContext

from django.http import HttpResponseRedirect

from django.core import serializers

from main_tables.models import *

from .forms import SysSyaAccountForm

import Cookie

from .functions import *

from django.shortcuts import get_object_or_404

from django.views.generic import ListView

 

# Create your views here.

def module(request, value):

	cookie = request.COOKIES.get("new_cook")
	mod = SysSymModule.objects.filter(sym_id=value).exclude(sym_folder = None)
	params = request.GET
	check = []

	if len(mod) > 0:
		module = mod[0]
		view = "ckbe/modules/{module.sym_folder}/index.html".format(**locals())
		# view = "ckbe/modules/%s/index.html" % { str(module.sym_folder) } 
	
	if cookie:

		account = SysSyaAccount.objects.filter(sya_id=cookie)[0]
		modules = account.sys_sym_modules.all()
		
		for x in modules:
			if (x.sym_id == int(value)) and (x.sym_folder != None):
				check.append(x)

	if (len(check) > 0):

		context = {
			"cookie": cookie,
			"module": module,
			"params": params,
			"view": view,
		}

		return render(request, "module.html", context)

	else:
		
		return HttpResponseRedirect("/", locals())

	

def home(request):

	if request.method == "POST":

		u_name = request.POST.get("sya_name")
		u_password = request.POST.get("sya_password")
		form = SysSyaAccountForm(initial={"sya_name":"%(u_name)s" % { "u_name":u_name}, "sya_password":"%(u_password)s" % {"u_password":u_password} })

		#::USING RAW SQL::
		# cursor = connection.cursor()
		# sql_query = cursor.execute("SELECT * FROM  sys_sya_account WHERE sya_name=%s AND sya_password=%s", (u_name, u_password,))
		# rows = sql_query.fetchall()
		# rows_length = len(rows)

		query = run_query("SELECT * FROM  sys_sya_account WHERE sya_name=%s AND sya_password=%s", u_name, u_password)
		
		#::USING ORM::
		# query = SysSyaAccount.objects.filter(sya_name="%(u_name)s" % {"u_name":u_name}).filter(sya_password="%(u_password)s" % {"u_password":u_password})
		# length = len(query)

		if query["length"] > 0:

			for row in query["rows"]:
				u_id = row.sya_id

			response = HttpResponseRedirect("/", locals())
			response.set_cookie("new_cook", "%d" % (u_id), max_age = 50000)
			return response

		else:

			error = "User not found"
			return	render_to_response("home.html", 
					locals(), 
					context_instance=RequestContext(request))

	else:

		form = SysSyaAccountForm()
		return	render_to_response("home.html",								 
				locals(), 
				context_instance=RequestContext(request))




