# Generated by Django 4.1.4 on 2023-01-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_genre_remove_film_genre_film_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images_persons/', verbose_name='Фото')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('films', models.ManyToManyField(to='films.film')),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
            },
        ),
    ]
