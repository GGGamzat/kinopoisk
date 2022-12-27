from django.urls import path
from . import views

urlpatterns = [
    path('', views.films, name='films'),
    path('<int:film_id>/', views.films),
    path('comedy/', views.comedys),
    path('comedy/<int:comedy_id>/', views.comedy),
    # path('cartoon/', views.cartoon),
    # path('thriller/', views.thriller),
    # path('fantasy/', views.fantasy),
]
