from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

# Create your views here.

def indexAgent(request):
    context={}
    return render(request, 'interfaces/agent/indexAgent.html', context)

def livraisonCarburant(request):
    gestionCarburant = Entblcarburant
    context={'gestionCarburant' : gestionCarburant}
    return render(request, 'interfaces/agent/GestionCarburant/livraisonCarburant.html', context)

@csrf_exempt
def creerLivraison(request):
    if request.method == 'POST':
        print('post')
        livraisonForm = LivraisonForm(request.POST)
        if livraisonForm.is_valid():
            user = livraisonForm.save()
            user.refresh_from_db()
            print(user)
            auth_login(request, user)
            return redirect('index')
    else:
        print('get')
        livraisonForm = LivraisonForm()
    context={'livraisonForm' : livraisonForm}
    return render(request, 'interfaces/agent/GestionCarburant/livraisonCarburant.html', context)

def mvtPompes(request):
    context={}
    return render(request, 'interfaces/agent/GestionCarburant/mvtPompes.html', context)

def ctrlStockCarburant(request):
    context={}
    return render(request, 'interfaces/agent/GestionCarburant/ctrlStockCarburant.html', context)

def indexAdmin(request):
    context={}
    return render(request, 'interfaces/administ/indexAdmin.html', context)

@csrf_exempt
def enregistrement(request):
    print(request.method)
    if request.method == 'POST':
        print('test')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            print(user)
            auth_login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
        print(form)
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
