from django.shortcuts import render, get_object_or_404
from .models import Film, Genre, Person


def getFilms(request):
    films = Film.objects.all()
    return render(request, 'films/films.html', {'films': films})


def getFilm(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'films/film.html', {'film': film})


def getComedys(request):
    comedys = Film.objects.filter(name='комедия')
    return render(request, 'films/comedys.html', {'comedys': comedys})


def getCartoons(request):
    cartoons = Film.objects.filter(genre='мультфильм')
    return render(request, 'films/cartoons.html', {'cartoons': cartoons})


def getThrillers(request):
    thrillers = Film.ojects.filter(genre='триллер')
    return render(request, 'films/thrillers.html', {'thrillers': thrillers})


def getFantasys(request):
    fantasys = Film.objects.filter(genre='фантастика')
    return render(request, 'films/fantasys.html', {'fantasys': fantasys})


def test(request):
    persons = Person.objects.all()
    return render(request, 'films/test.html', {'persons': persons})