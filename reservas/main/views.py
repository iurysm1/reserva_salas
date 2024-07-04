from django.shortcuts import render, redirect
from .models import Sala, Cadeira
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

    




def home(request):
    salas = Sala.objects.all()
    return render(request, 'main/home.html', {'salas':salas})

@login_required()
def sala(request, id):
    sala = Sala.objects.get(id=id)
    if request.method=='POST':
        if request.POST.get('confirmar'):
            for cadeira in sala.cadeira_set.all():
                if request.POST.get("cadeira"+str(cadeira.id)) == "clicked":
                    cadeira.status=True
                    cadeira.user_id=request.user.id
                cadeira.save()
        elif request.POST.get('limpar'):
            for cadeira in sala.cadeira_set.all():
                if cadeira.user_id==request.user.id:
                    cadeira.status=False
                    cadeira.user_id=None
                cadeira.save()
        return render(request, 'main/sala.html', {"sala":sala})

    return render(request, 'main/sala.html', {"sala":sala})


def cadeiras(request,id):
    sala=Sala.objects.get(id=id)
    cadeiras=Sala.objects.get(id=sala.id).cadeira_set.all()
    cadeiras_json=[]

    for cadeira in cadeiras:
        novaCadeira = {'id': cadeira.id, 'numeroCadeira':cadeira.numeroCadeira, 'andar': cadeira.andar, 'status':cadeira.status, 'user_id':cadeira.user_id, 'user_request':request.user.id}
        cadeiras_json.append(novaCadeira)
    return JsonResponse({'cadeiras':cadeiras_json})






