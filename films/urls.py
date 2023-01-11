from django.urls import path
from . import views

urlpatterns = [
    path('', views.getFilms, name='films'),
    path('<int:film_id>/', views.getFilm, name='film'),
    path('comedy/', views.getComedys),
    path('cartoon/', views.getCartoons),
    # path('test/', views.test),
    path('thriller/', views.getThrillers),
    # path('fantasy/', views.fantasy),
]
