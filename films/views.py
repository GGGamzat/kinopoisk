from django.shortcuts import render
from .models import Film


def films(request):
    films = Film.objects.all()
    return render(request, 'films/films.html', {'films': films})


def film(request, film_id):
    film = Film.objects.get(pk=film_id)
    return render(request, 'films/film.html', {'film': film})


def comedys(request):
    comedys = Film.objects.filter(genre='комедия')
    return render(request, 'films/comedys.html', {'comedys': comedys})


def comedy(request, comedy_id):
    comedy = Film.objects.get(pk=comedy_id)
    return render(request, 'films/comedy.html', {'comedy': comedy})


# def cartoons(request):
#     cartoons = Film.objects.filter(genre='мультфильм')
#     return render(request, 'films/cartoon.html', {'cartoons': cartoons})