from django.shortcuts import render
from .models import Film


def getFilms(request):
    films = Film.objects.all()
    return render(request, 'films/films.html', {'films': films})


def getFilm(request, film_id):
    film = Film.objects.get(pk=film_id)
    return render(request, 'films/film.html', {'film': film})


def getComedys(request):
    comedys = Film.objects.filter(genre='комедия')
    return render(request, 'films/comedys.html', {'comedys': comedys})


def getCartoons(request):
    cartoons = Film.objects.filter(genre='мультфильм')
    return render(request, 'films/cartoons.html', {'cartoons': cartoons})


def getThrillers(request):
    thrillers = Film.ojects.filter(genre='триллер')
    return render(request, 'films/thrillers.html', {'thrillers': thrillers})


# def test(request):
#     b = Film.objects.get(pk=1)
#     b.name = "Аманат"
#     b.save()
#     return render(request, 'films/test.html', {'b': b})