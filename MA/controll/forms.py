from django import forms
from .models import client

class ClientRegisterForm(forms.ModelForm):
	nickName = forms.CharField(widget = forms.TextInput(
		attrs = {
			'class': 'form-control',
			'id': 'exampleInputText1',
			'name': 'nickName',
			'placeholder': 'Enter nick name',
		}
	))

	email = forms.CharField(widget = forms.EmailInput(
		attrs = {
			'class': 'form-control',
			'id': 'exampleInputEmail1',
			'name': 'email',
			'aria-describedby': 'emailHelp',
			'placeholder': 'Enter email',
		}
	))

	password = forms.CharField(widget = forms.PasswordInput(
		attrs = {
			'class': 'form-control',
			'id': 'exampleInputPassword1',
			'name': 'password',
			'placeholder': 'Enter password',
		}
	))

	class Meta:
		model = client
		fields = ('email', 'nickName', 'password',)