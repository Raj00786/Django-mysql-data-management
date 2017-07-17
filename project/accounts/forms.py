from django import forms
from django.contrib.auth import (authenticate,get_user_model,login,logout)
from django.core.validators import RegexValidator

User = get_user_model()
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class UserLoginForm(forms.Form):
	username = forms.CharField(validators=[alphanumeric])
	password = forms.CharField(widget =forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		if not user:
			raise forms.ValidationError('This user doesn"t exist')
		if not user.check_password(password):
			raise forms.ValidationError('Incorrect Password')
		if not user.is_active:
			raise forms.ValidationError('This user is no longer active')
		return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(validators=[alphanumeric])
	password = forms.CharField(label = 'Password',widget =forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password',widget =forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password",
			"password2"
		]

	def clean_password2(self):
		print(self.cleaned_data)
		email = self.cleaned_data.get('email')
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		print(password2,password1)
		if password1 != password2:
			raise forms.ValidationError('Password must match')

		email_qs = User.objects.filter(email = email)
		if email_qs.exists():
			raise forms.ValidationError('This email is already linked with another account')
		return email

class ForgotForm(forms.Form):
	username = forms.CharField(validators=[alphanumeric])
	email = forms.EmailField()

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		if not username:
			raise forms.ValidationError('This user doesn"t exist')
