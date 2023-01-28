from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Film, Genre, Person


class getFilms(ListView):
    model = Film
    template_name = 'films/films.html'
    context_object_name = 'films'


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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['genre'] = str(context['genres'][0].name)
    #     return context


# def getGenre(request, slug):
#     genres = Film.objects.filter(genre__slug=slug)
#     return render(request, 'films/genres.html', {'genres': genres})


# def test(request):
#     persons = Person.objects.all()
#     return render(request, 'films/test.html', {'persons': persons})