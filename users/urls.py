from django.urls import path
from . import views

urlpatterns = [
	path('', views.users),
	path('register/', views.register),
	path('login/', views.login),
	path('logout/', views.logout),
	path('profile/', views.profile),
]