from django.shortcuts import render
from .models import Cars

def home(request):
    cars = Cars.objects.all()
    contex = {'cars': cars}
    return render(request, 'index.html', contex)
