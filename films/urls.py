from django.urls import path
from . import views

urlpatterns = [
    path('', views.getFilms, name='films'),
    path('<int:film_id>/', views.getFilm, name='film'),
    path('comedy/', views.getComedys),
    path('cartoon/', views.getCartoons),
    path('thriller/', views.getThrillers),
    path('fantasy/', views.getFantasys),
    path('test/', views.test),
]
