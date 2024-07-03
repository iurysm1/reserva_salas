from django.shortcuts import render, redirect
from .models import Sala, Cadeira
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def home(request):


   
    return render(request, 'main/home.html')


def sala(request, id):


    return render(request, 'main/sala.html')


def cadeiras(request):
    cadeiras=Sala.objects.get(id=2).cadeira_set.all()
    cadeiras_json=serializers.serialize('json', cadeiras)
    return JsonResponse({'cadeiras':cadeiras_json})

