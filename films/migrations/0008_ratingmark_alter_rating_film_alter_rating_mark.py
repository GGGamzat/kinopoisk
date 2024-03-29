# Generated by Django 4.2.1 on 2023-07-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_alter_comment_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.SmallIntegerField(verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.AlterField(
            model_name='rating',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film', unique=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.ratingmark'),
        ),
    ]
