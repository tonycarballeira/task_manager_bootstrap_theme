from django.contrib import admin

# Register your models here.
from .models import SysSymModule, SysSyaAccount, SysRlnSyaSym

class AccountAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "sya_name"]
	class Meta:
		model = SysSyaAccount

admin.site.register(SysSymModule)
admin.site.register(SysSyaAccount, AccountAdmin)
admin.site.register(SysRlnSyaSym)
