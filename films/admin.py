from django.contrib import admin
from .models import Film, Genre

# admin.site.register(Film)
admin.site.register(Genre)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ['genre']
    search_fields = ['name']


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     filter_horizontal = ['films']
#     search_fields = ['name']