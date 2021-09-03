from django.shortcuts import render
from .models import Transacao
import datetime

def home(request):
   data = {}
   data['transacoes'] = Transacao.objects.all()

   return render(request, 'templates/home.html', data)