from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver


def users(request):
	users = User.objects.all()
	return render(request, 'users/users.html', {'users': users})


def login(request):
	email = request.POST['email']
	password = request.POST['password']
	user = authenticate(request, email=email, password=password)
	if user is not None:
		login(request, user)
		return render(request, 'users/profile.html')
	else:
		return render(request, 'users/login.html')


def logout(request):
	logout(request)
	return render(request, 'main/main.html')


def register(request):
	return render(request, 'users/register.html')


@receiver
@login_required(login_url="/users/login/")
def profile(request):
	return render(request, 'users/profile.html')