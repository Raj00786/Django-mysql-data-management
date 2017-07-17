from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib.auth import (authenticate,get_user_model,login,logout)
from .forms import UserLoginForm,UserRegisterForm,ForgotForm
# Create your views here.
def login_view(request):
	print(request.user.is_authenticated())		
	title = 'Login'
	form = UserLoginForm(request.POST or None)
	if form.is_valid():

		# subject = 'Registration mail'
		# message = 'Thank you for your registration and member of our company kritsnam technology '
		# from_email = 'rajkumarmeena259996@gmail.com'
		# to = ['rajmeena@iitk.ac.in']
		# send_mail(subject,message,from_email,to,fail_silently=True)

		messages.success(request,"User Logged In Successfully")

		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		login(request,user)
		return redirect('/')
	return render(request,"blogs/account_form.html",{"form":form,"title":title})


def register_view(request):
	title = 'Register'
	form = UserRegisterForm(request.POST or None) 
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		return redirect('/')


	return render(request,"blogs/account_form.html",{"form":form,"title":title})

def logout_view(request):
	messages.success(request,"User Logged Out Successfully")
	logout(request)
	return redirect('/login')

def forgot_view(request):
	title = 'Resend Mail'
	form = ForgotForm(request.POST or None)
	if form.is_valid():

		subject = 'Forgot Password'
		message = 'Thank you for your registration and member of our company kritsnam technology '
		from_email = 'rajkumarmeena259996@gmail.com'
		to = ['rajmeena@iitk.ac.in']
		send_mail(subject,message,from_email,to,fail_silently=True)

		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		return redirect('/')
	return render(request,"blogs/account_form.html",{"form":form,"title":title})
