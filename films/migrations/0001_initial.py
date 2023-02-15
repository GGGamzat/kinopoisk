# Generated by Django 4.1.4 on 2023-02-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя жанра')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'Genre',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images_films/', verbose_name='Изображение')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('country', models.CharField(choices=[('U', 'США'), ('R', 'Россия'), ('UK', 'Великобритания'), ('F', 'Франция'), ('N', 'Япония')], max_length=50, verbose_name='Страна')),
                ('director', models.CharField(max_length=50, verbose_name='Режиссёр')),
                ('genre', models.ManyToManyField(to='films.genre')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'db_table': 'Film',
            },
        ),
    ]
