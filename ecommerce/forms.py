from django import forms
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control",
			"placeholder":"Your fullname"
			}
			 )
		)
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
			"class":"form-control",
			 "placeholder":"email"
			 }
			 )
		)
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class":"form-control", "placeholder":"content here"
			}
			)
		)
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "@gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail.com")
			return email
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'fullname'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'gmail.com' in email:
			raise forms.ValidationError("email has to be gmail")
			return email
class RegisterForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	email = forms.CharField()
	def clean(self):
		data = self.cleaned_data
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Passwords do not match")
			return data
	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username already exists")
		return username



	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Passwords do not match")
			return data
	























