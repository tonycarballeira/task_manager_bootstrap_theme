from django.shortcuts import render, render_to_response, RequestContext

from django.core import serializers

from main_tables.models import *

from .forms import SysSyaAccountForm

 

# Create your views here.
def home(request):
	
	account = "Modules"
	context = {
		"template_title": account,
		"data": SysSyaAccount.objects.filter(sya_id=7)[0].sys_sym_modules.all()
	}
	return render(request, "home.html", context)

def sign_in(request):
	form = SysSyaAccountForm()
	return render_to_response("signin.html", 
							   locals(), 
							   context_instance=RequestContext(request))