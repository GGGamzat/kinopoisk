from querybuilder.query import Query
from django.db import connection
from collections import namedtuple

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Film, Genre


class getFilms(ListView):
    model = Film
    template_name = 'films/films.html'
    context_object_name = 'films'


# def test(request):
#     films = Film.objects.all()
#     return render(request, 'films/test.html', {'films': films})


class getFilm(DetailView):
    model = Film
    template_name = 'films/film.html'
    context_object_name = 'film'
    pk_url_kwarg = 'film_id'


class getGenre(ListView):
    model = Film
    template_name = 'films/genres.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Film.objects.filter(genre__slug=self.kwargs['slug'])


# def getGenre(request, slug):
#     genres = Film.objects.filter(genre__slug=slug)
#     return render(request, 'films/genres.html', {'genres': genres})


# def test(request):
#     cur = connection.cursor()
#     cur.execute('SELECT * FROM "Film"')
#     films = cur.fetchall()
#     result = namedtuple('Result', 'id image name text country director')
#     films = result(films[0][0], films[0][1], films[0][2], films[0][3], films[0][4], films[0][5])
#     return render(request, 'films/test.html', {'films': films})

# def namedtuplefetchall(cursor):
#     desc = cursor.description
#     result = namedtuple('')


# def test(request):
#     query = Query().from_table('"Film"')
#     films = query.select()
#     return render(request, 'films/test.html', {'films': films})


# def test(request):
#     films = Film.objects.raw('SELECT * FROM "Film"')
#     return render(request, 'films/test.html', {'films': films})