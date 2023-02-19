from django import forms
from django.forms import ModelForm

from .models import CustomUser


class RegisterForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter username'}), max_length=50)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter email'}), max_length=100)
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter phone'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'phone']

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd ['password2']:
			raise forms.ValidationError('Password don\'t match')
		return cd['password2']