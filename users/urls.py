from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login.as_view(), name='login'),
	# path('login/', views.login),
	path('logout/', views.logout),
	path('profile/', views.profile, name='profile'),
]