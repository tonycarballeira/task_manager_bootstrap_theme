"""python_manage3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r"^$", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r"^$", Home.as_view(), name="home")
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r"^blog/", include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView
from main_tables.models import *
import Cookie

import main_tables.views



urlpatterns = [
	url(r"^$", main_tables.views.sign_in),
    url(r"^sign_in$", main_tables.views.sign_in),
    url(r"^(\d+)", main_tables.views.module, name="module"),

    # url(r'^modules$', ListView.as_view( model=SysSymModule, template_name="modules.html", context_object_name="sys_sym_modules", )),
]

# urlpatterns = patterns('',
#     (r'^modules/$', ListView.as_view(
#         model=SysSymModule,
#         template_name='modules.html'
#     )),
# )


 # url(r"^admin/", include(admin.site.urls)),