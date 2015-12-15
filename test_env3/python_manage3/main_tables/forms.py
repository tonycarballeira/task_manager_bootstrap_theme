from django import forms

from .models import SysSyaAccount

class SysSyaAccountForm(forms.ModelForm):
	class Meta:
		model = SysSyaAccount
		fields = "sya_name", "sya_password"