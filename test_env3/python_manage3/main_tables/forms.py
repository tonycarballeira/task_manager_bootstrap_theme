from django import forms

from .models import SysSyaAccount

class SysSyaAccountForm(forms.ModelForm):
	class Meta:
		model = SysSyaAccount
		fields = '__all__'