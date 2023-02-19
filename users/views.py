from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from .forms import RegisterForm
from django.urls import reverse_lazy

from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from .models import CustomUser
from django.contrib.auth import authenticate, login
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


class login(LoginView):
	template_name = 'users/login.html'
	redirect_field_name = 'users/profile.html'


# def login(request):
# 	email = request.POST['email']
# 	password = request.POST['password']
# 	user = authenticate(request, email=email, password=password)
# 	if user is not None:
# 		login(request, user)
# 		return render(request, 'users/profile.html')
# 	else:
# 		return render(request, 'users/login.html')


def logout(request):
	logout(request)
	return render(request, 'main/main.html')


# @receiver
# @login_required(login_url="/users/login/")
def profile(request):
	return render(request, 'users/profile.html')