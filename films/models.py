from django.db import models


class Genre(models.Model):
    name = models.CharField('Имя жанра', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(models.Model):
    image = models.ImageField('Изображение', upload_to='images_films/')
    name = models.CharField('Название', max_length=50)
    genre = models.ManyToManyField(Genre)
    text = models.TextField('Описание')
    country = models.CharField('Страна', max_length=50)
    director = models.CharField('Режиссёр', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


# class Film_genre(models.Model):
#     film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
#     genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Person(models.Model):
    image = models.ImageField('Фото', upload_to='images_persons/')
    name = models.CharField('Имя', max_length=50)
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
