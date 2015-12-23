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
	module = SysSymModule.objects.filter(sym_id=value)

	context = {
		"cookie": cookie,
		"module": module,
	}

	return render(request, "module.html", context)


def sign_in(request):

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
			return	render_to_response("signin.html", 
					locals(), 
					context_instance=RequestContext(request))

	else:

		form = SysSyaAccountForm()
		return	render_to_response("signin.html",								 
				locals(), 
				context_instance=RequestContext(request))


def home(request):

	cookie = request.COOKIES.get("new_cook")
	account = "Modules"

	context = {
		"template_title": account,
		"cookie": cookie,
	}

	return render(request, "home.html", context)

