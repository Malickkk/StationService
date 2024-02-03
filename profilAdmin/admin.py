from django.contrib import admin

from .models import *
# Register your models here.
mesModels = [Stationservice, Article, Client, Utilisateur]
admin.site.register(mesModels)