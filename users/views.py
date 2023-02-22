from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy

from django.views.generic import CreateView

from django.contrib.auth.views import LogoutView
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			return redirect('profile')
		else:
			return HttpResponse('Данные не верны')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form})


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(email=cd['email'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'users/profile.html')
				else:
					return HttpResponse('Отключённая учётная запись')
			else:
				return HttpResponse('Неверный логин или пароль.')
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('main')


# @receiver
# @login_required(login_url="/users/login/")
def profile(request):
	return render(request, 'users/profile.html')