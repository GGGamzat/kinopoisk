from django.db import models


class Film(models.Model):
    image = models.ImageField('Изображение', upload_to='images_films/')
    name = models.CharField('Название', max_length=50)
    genre = models.CharField('Жанр', max_length=50)
    text = models.TextField('Описание')
    country = models.CharField('Страна', max_length=50)
    director = models.CharField('Режиссёр', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
