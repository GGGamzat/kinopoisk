import datetime
from querybuilder.query import Query
from django.db import connection
from collections import namedtuple

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Film, Genre
from users.models import UserSubscription, Subscription


class getFilms(ListView):
    model = Film
    template_name = 'films/films.html'
    context_object_name = 'films'


# class getFilm(DetailView):
#     model = Film
#     template_name = 'films/film.html'
#     context_object_name = 'film'
#     pk_url_kwarg = 'film_id'


def film(request, film_id):
    film = Film.objects.get(pk=film_id)
    subscription = Subscription.objects.get(name='"Кино Плюс"')

    try:
        sub = UserSubscription.objects.get(user=request.user)
    except UserSubscription.DoesNotExist:
        sub = None

    if film.by_subscription == 'Да':
        if sub is None:
            return render(request, 'films/pay_film.html', {'film': film})
        elif sub is not None:
            date_now = datetime.date.today()
            year = sub.date.year
            month = sub.date.month
            day = sub.date.day
            date = datetime.date(year, month, day)
            check = (date_now - date).days
            if check <= subscription.time_limit:
                return render(request, 'films/film.html', {'film': film})
            else:
                return render(request, 'films/pay_film.html', {'film': film})
    else:
        return render(request, 'films/film.html', {'film': film})


class getGenre(ListView):
    model = Film
    template_name = 'films/genres.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Film.objects.filter(genre__slug=self.kwargs['slug'])