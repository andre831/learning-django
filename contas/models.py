from django.db import models
from django.db.models.fields import CharField, EmailField

class Categoria(models.Model):

    nome = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    