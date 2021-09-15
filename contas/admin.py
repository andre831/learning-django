from calendar import c
from django.contrib import admin
from .models import Categoria, Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)