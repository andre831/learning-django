from django.shortcuts import render
import datetime

from django.utils.timezone import now

def home(request):
   now = datetime.datetime.now()
   return render(request, 'templates/home.html')