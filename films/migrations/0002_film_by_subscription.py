# Generated by Django 4.1.7 on 2023-03-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='by_subscription',
            field=models.CharField(choices=[('Y', 'Да'), ('N', 'Нет')], default='Нет', max_length=10, verbose_name='По подписке'),
        ),
    ]
