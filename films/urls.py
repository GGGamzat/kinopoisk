from django.urls import path
from . import views

urlpatterns = [
    path('', views.films, name='films'),
    path('<int:film_id>/', views.film),
    path('comedys/', views.comedys),
    path('comedys/<int:comedy_id>/', views.comedy),
    # path('cartoon/', views.cartoon),
    # path('thriller/', views.thriller),
    # path('fantasy/', views.fantasy),
]
