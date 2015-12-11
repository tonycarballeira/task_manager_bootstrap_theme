from django.contrib import admin

from django import forms

# Register your models here.
from .models import SysSymModule, SysSyaAccount, SysRlnSyaSym

# class AccountAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__", "sya_name"]
# 	class Meta:
# 		model = SysSyaAccount

# admin.site.register(SysSymModule)
# admin.site.register(SysSyaAccount, AccountAdmin)
# admin.site.register(SysRlnSyaSym)

# class UserCreationForm(forms.ModelForm):
# 	password1 = forms.CharField(label = 'Type Password', widget = forms.PasswordInput)
# 	password2 = forms.CharField(label = 'Re - Type Password', widget = forms.PasswordInput)

# 	class Meta:
# 		model = SysSyaAccount
# 		fields = ['sya_email', 'sya_password',]


# 		def clean_password(self):
# 			password1 = self.cleaned_data['password1']
# 			password2 = self.cleaned_data['password2']
# 			if password1 and password2 and password1 != password2:
# 				raise formsValidationError('Password Does not match')
# 			return password2

# 		def save(self, commit = True):
# 			user = Super(UserCreationForm, self).save(commit = False)
# 			user.set_password(self.cleaned_data['password1'])
# 			user.save()
# 			return user
