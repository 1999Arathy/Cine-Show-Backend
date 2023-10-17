from django.contrib import admin

from .models import Movie, usermodel

# Register your models here.
admin.site.register(Movie)
admin.site.register(usermodel)