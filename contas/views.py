from django.shortcuts import redirect, render
from .models import Transacao
from .form import TransacaoForm
from contas import form


def home(request):
   data = {}
   data['transacoes'] = Transacao.objects.all()

   return render(request, 'templates/home.html', data)

def add_nova_transacao(request):
   form = TransacaoForm(request.POST or None)

   data = {}
   data['form'] = form

   if form.is_valid():
      form.save()
      return redirect('home')

   return render(request, 'templates/form.html', data)