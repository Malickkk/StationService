from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

# Create your views here.

folderLocation = 'interfaces/administ/parametreDeBase/'

def indexAdmin(request):
    context={}
    return render(request, 'interfaces/administ/indexAdmin.html', context)

# ************* Section Station Services *************

def stationServices(request):
    stationServices = Stationservice.objects.all()
    context={'values' : stationServices}
    return render(request, folderLocation+'index/stationServices.html', context)

@csrf_exempt
def stationCreate(request):
    if request.method == 'POST':
        creerStationForm = stationServiceForm(request.POST)
        if creerStationForm.is_valid():
            creerStationForm.save()
            return redirect('stationServices')
    else:
        creerStationForm = stationServiceForm()
    context={'creerStationForm' : creerStationForm}
    return render(request, folderLocation+'create/stationCreate.html', context)

@csrf_exempt
def stationEdit(request, pk):
    station = get_object_or_404(Stationservice, idstation=pk)
    modifierStation = stationServiceForm(request.POST or None, instance=station)
    if modifierStation.is_valid():
        modifierStation.save()
        return redirect('stationServices')
    context = {'modifierStation': modifierStation}
    return render(request, folderLocation+'edit/stationEdit.html', context)

@csrf_exempt
def stationInfo(request, pk):
    station = Stationservice.objects.get(idstation=pk)
    infostation = stationServiceForm(request.POST or None, instance=station)
    context = {'infostation': infostation}
    return render(request, folderLocation+'info/stationInfo.html', context)

@csrf_exempt
def stationDelete(request, pk):
    station = get_object_or_404(Stationservice, idstation=pk)
    if request.method == 'POST':
        station.delete()
        return redirect('stationServices')
    context = {'station': station}
    return render(request, folderLocation+'delete/stationDelete.html', context)


# ************* Section Utilisateurs *************

def users(request):
    utilisateurs = Utilisateur.objects.all()
    context={'values' : utilisateurs}
    return render(request, folderLocation+'index/users.html', context)

@csrf_exempt
def userCreate(request):
    if request.method == 'POST':
        creerUserForm = utilisateurForm(request.POST or None)
        if creerUserForm.is_valid():
            creerUserForm.save()
            return redirect('users')
    else:
        creerUserForm = utilisateurForm()
    context={'creerUserForm' : creerUserForm}
    return render(request, folderLocation+'create/userCreate.html', context)

@csrf_exempt
def userEdit(request, pk):
    user = get_object_or_404(Utilisateur, iduser=pk)
    modifierUser = utilisateurForm(request.POST or None, instance=user)
    if modifierUser.is_valid():
        modifierUser.save()
        return redirect('users')
    context = {'modifierUser': modifierUser}
    return render(request, folderLocation+'edit/userEdit.html', context)

@csrf_exempt
def userInfo(request, pk):
    user = Utilisateur.objects.get(iduser=pk)
    infoUser = utilisateurForm(request.POST or None, instance=user)
    context = {'infoUser': infoUser}
    return render(request, folderLocation+'info/userInfo.html', context)

@csrf_exempt
def userDelete(request, pk):
    user = get_object_or_404(Utilisateur, iduser=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {'user': user}
    return render(request, folderLocation+'delete/userDelete.html', context)


# ************* Section articles *************

def articles(request):
    articles = Article.objects.all()
    context={'values' : articles}
    return render(request, folderLocation+'index/articles.html', context)

@csrf_exempt
def creerArticle(request):
    if request.method == 'POST':
        creerarticleForm = Article(request.POST)
        if creerarticleForm.is_valid():
            creerarticleForm.save()
            return redirect('articles')
    else:
        creerarticleForm = articleForm()
    context={'creerarticleForm' : creerarticleForm}
    return render(request, folderLocation+'create/articleCreate.html', context)

@csrf_exempt
def articleEdit(request, pk):
    article = get_object_or_404(Article, idarticle=pk)
    modifierarticle = articleForm(request.POST or None, instance=article)
    if modifierarticle.is_valid():
        modifierarticle.save()
        return redirect('articles')
    context = {'modifierarticle': modifierarticle}
    return render(request, folderLocation+'edit/articleEdit.html', context)

@csrf_exempt
def articleInfo(request, pk):
    article = Article.objects.get(idarticle=pk)
    infoarticle = articleForm(request.POST or None, instance=article)
    context = {'infoarticle': infoarticle}
    return render(request, folderLocation+'info/articleInfo.html', context)

@csrf_exempt
def articleDelete(request, pk):
    article = get_object_or_404(Article, idarticle=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    context = {'article': article}
    return render(request, folderLocation+'delete/articleDelete.html', context)


# ************* Section Tarifs *************

def tarifs(request):
    tarifs = Tarif.objects.all()
    context={'values' : tarifs}
    return render(request, folderLocation+'index/tarifs.html', context)

@csrf_exempt
def tarifCreate(request): #verifier que les dates ne se chevauchent pas
    if request.method == 'POST':
        creerTarifForm = tarifForm(request.POST)
        if creerTarifForm.is_valid():
            creerTarifForm.save()
            return redirect('tarifs')
    else:
        creerTarifForm = tarifForm()
    context={'creerTarifForm' : creerTarifForm}
    return render(request, folderLocation+'create/tarifCreate.html', context)

@csrf_exempt
def tarifEdit(request, pk):
    tarif = get_object_or_404(Tarif, idtarif=pk)
    modifierTarif = tarifForm(request.POST or None, instance=tarif)
    if modifierTarif.is_valid():
        modifierTarif.save()
        return redirect('tarifs')
    context = {'modifierTarif': modifierTarif}
    return render(request, folderLocation+'edit/tarifEdit.html', context)

@csrf_exempt
def tarifInfo(request, pk):
    tarif = Tarif.objects.get(idtarif=pk)
    infoTarif = tarifForm(request.POST or None, instance=tarif)
    print(tarif.datedebut - tarif.datefin)
    context = {'infoTarif': infoTarif}
    return render(request, folderLocation+'info/tarifInfo.html', context)

@csrf_exempt
def tarifDelete(request, pk):
    tarif = get_object_or_404(Tarif, idtarif=pk)
    if request.method == 'POST':
        tarif.delete()
        return redirect('tarifs')
    context = {'tarif': tarif}
    return render(request, folderLocation+'delete/tarifDelete.html', context)


# ************* Section Famille articles *************

def famillearticles(request):
    famillearticles = Famillearticle.objects.all()
    context={'values' : famillearticles}
    return render(request, folderLocation+'index/familleArticles.html', context)

@csrf_exempt
def famillearticleCreate(request):
    if request.method == 'POST':
        creerFamillearticleForm = famillearticleForm(request.POST)
        if creerFamillearticleForm.is_valid():
            creerFamillearticleForm.save()
            return redirect('famillearticles')
    else:
        creerFamillearticleForm = famillearticleForm()
    context={'creerFamillearticleForm' : creerFamillearticleForm}
    return render(request, folderLocation+'create/familleArticleCreate.html', context)

@csrf_exempt
def famillearticleEdit(request, pk):
    famillearticle = get_object_or_404(famillearticles, idfamille=pk)
    modifierFamillearticle = famillearticleForm(request.POST or None, instance=famillearticle)
    if modifierFamillearticle.is_valid():
        modifierFamillearticle.save()
        return redirect('famillearticles')
    context = {'modifierFamillearticle': modifierFamillearticle}
    return render(request, folderLocation+'edit/familleArticleEdit.html', context)

@csrf_exempt
def famillearticleInfo(request, pk):
    famillearticle = famillearticles.objects.get(idfamille=pk)
    infofamillearticle = famillearticleForm(request.POST or None, instance=famillearticle)
    context = {'infofamillearticle': infofamillearticle}
    return render(request, folderLocation+'info/familleArticleInfo.html', context)

@csrf_exempt
def famillearticleDelete(request, pk):
    famillearticle = get_object_or_404(famillearticles, idfamille=pk)
    if request.method == 'POST':
        famillearticle.delete()
        return redirect('famillearticles')
    context = {'famillearticle': famillearticle}
    return render(request, folderLocation+'delete/familleArticleDelete.html', context)


# ************* Section Tarifs Clients *************

def clients(request):
    client = Client.objects.all()
    context={'values' : client}
    return render(request, folderLocation+'index/client.html', context)

@csrf_exempt
def clientCreate(request):
    if request.method == 'POST':
        creerClient = clientForm(request.POST)
        if creerClient.is_valid():
            creerClient.save()
            return redirect('clients')
    else:
        creerClient = clientForm()
    context={'creerClient' : creerClient}
    return render(request, folderLocation+'create/clientCreate.html', context)

@csrf_exempt
def clientEdit(request, pk):
    Client = get_object_or_404(Client, idcli=pk)
    modifierClient = clientForm(request.POST or None, instance=Client)
    if modifierClient.is_valid():
        modifierClient.save()
        return redirect('clients')
    context = {'modifierClient': modifierClient}
    return render(request, folderLocation+'edit/clientEdit.html', context)

@csrf_exempt
def clientInfo(request, pk):
    Client = Client.objects.get(idcli=pk)
    infoClient = clientForm(request.POST or None, instance=Client)
    context = {'infoClient': infoClient}
    return render(request, folderLocation+'info/clientInfo.html', context)

@csrf_exempt
def clientDelete(request, pk):
    client = get_object_or_404(Client, idcli=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')
    context = {'client': client}
    return render(request, folderLocation+'delete/clientDelete.html', context)


# ************* Section Tarifs Clients *************

def tarifClient(request):
    tarifsClient = TarifsClient.objects.all()
    context={'values' : tarifsClient}
    return render(request, folderLocation+'index/tarifClient.html', context)

@csrf_exempt
def tarifClientCreate(request):
    if request.method == 'POST':
        creerTarifClient = tarifClientForm(request.POST)
        if creerTarifClient.is_valid():
            creerTarifClient.save()
            return redirect('tarifClient')
    else:
        creerTarifClient = tarifClientForm()
    context={'creerTarifClient' : creerTarifClient}
    return render(request, folderLocation+'create/tarifClientCreate.html', context)

@csrf_exempt
def tarifClientEdit(request, pk):
    tarifClient = get_object_or_404(TarifsClient, idtarcli=pk)
    modifierTarifClient = tarifClientForm(request.POST or None, instance=tarifClient)
    if modifierTarifClient.is_valid():
        modifierTarifClient.save()
        return redirect('tarifClient')
    context = {'modifierTarifClient': modifierTarifClient}
    return render(request, folderLocation+'edit/tarifClientEdit.html', context)

@csrf_exempt
def tarifClientInfo(request, pk):
    tarifClient = TarifsClient.objects.get(idtarcli=pk)
    infoTarifClient = tarifClientForm(request.POST or None, instance=tarifClient)
    context = {'infoTarifClient': infoTarifClient}
    return render(request, folderLocation+'info/tarifClientInfo.html', context)

@csrf_exempt
def tarifClientDelete(request, pk):
    tarifClient = get_object_or_404(TarifsClient, idtarcli=pk)
    if request.method == 'POST':
        tarifClient.delete()
        return redirect('tarifClient')
    context = {'tarifClient': tarifClient}
    return render(request, folderLocation+'delete/tarifClientDelete.html', context)


# ************* Section Fournisseurs *************

def fournisseurs(request):
    fournisseur = Fournisseur.objects.all()
    context={'values' : fournisseur}
    return render(request, folderLocation+'index/fournisseur.html', context)

@csrf_exempt
def fournisseurCreate(request):
    if request.method == 'POST':
        creerFournisseur = fournForm(request.POST)
        if creerFournisseur.is_valid():
            creerFournisseur.save()
            return redirect('fournisseurs')
    else:
        creerFournisseur = fournForm()
    context={'creerFournisseur' : creerFournisseur}
    return render(request, folderLocation+'create/fournisseurCreate.html', context)

@csrf_exempt
def fournisseurEdit(request, pk):
    fournisseur = get_object_or_404(Fournisseur, idfourn=pk)
    modifierFournisseur = fournForm(request.POST or None, instance=fournisseur)
    if modifierFournisseur.is_valid():
        modifierFournisseur.save()
        return redirect('fournisseurs')
    context = {'modifierFournisseur': modifierFournisseur}
    return render(request, folderLocation+'edit/fournisseurEdit.html', context)

@csrf_exempt
def fournisseurInfo(request, pk):
    fournisseur = Fournisseur.objects.get(idfourn=pk)
    infoFournisseur = fournForm(request.POST or None, instance=fournisseur)
    context = {'infoFournisseur': infoFournisseur}
    return render(request, folderLocation+'info/fournisseurInfo.html', context)

@csrf_exempt
def fournisseurDelete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, idfourn=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseurs')
    context = {'fournisseur': fournisseur}
    return render(request, folderLocation+'delete/fournisseurDelete.html', context)


# ************* Section Tarifs Fournisseurs *************

def tarifFournisseur(request):
    tarifFournisseur = Tarifsfourn.objects.all()
    context={'values' : tarifFournisseur}
    return render(request, folderLocation+'index/tarifFournisseur.html', context)

@csrf_exempt
def tarifFournisseurCreate(request):
    if request.method == 'POST':
        creerTarifFournisseur = tarifFournForm(request.POST)
        if creerTarifFournisseur.is_valid():
            creerTarifFournisseur.save()
            return redirect('tarifFournisseur')
    else:
        creerTarifFournisseur = tarifFournForm()
    context={'creerTarifFournisseur' : creerTarifFournisseur}
    return render(request, folderLocation+'create/tarifFournisseurCreate.html', context)

@csrf_exempt
def tarifFournisseurEdit(request, pk):
    tarifFournisseur = get_object_or_404(Tarifsfourn, idtarfourn=pk)
    modifierTarifFournisseur = tarifFournForm(request.POST or None, instance=tarifFournisseur)
    if modifierTarifFournisseur.is_valid():
        modifierTarifFournisseur.save()
        return redirect('tarifFournisseur')
    context = {'modifierTarifFournisseur': modifierTarifFournisseur}
    return render(request, folderLocation+'edit/tarifFournisseurEdit.html', context)

@csrf_exempt
def tarifFournisseurInfo(request, pk):
    tarifFournisseur = Fournisseur.objects.get(idtarfourn=pk)
    infoTarifFournisseur = tarifFournForm(request.POST or None, instance=tarifFournisseur)
    context = {'infoTarifFournisseur': infoTarifFournisseur}
    return render(request, folderLocation+'info/tarifFournisseurInfo.html', context)

@csrf_exempt
def tarifFournisseurDelete(request, pk):
    tarifFournisseur = get_object_or_404(Tarifsfourn, idtarfourn=pk)
    if request.method == 'POST':
        tarifFournisseur.delete()
        return redirect('tarifFournisseur')
    context = {'tarifFournisseur': tarifFournisseur}
    return render(request, folderLocation+'delete/tarifFournisseurDelete.html', context)


# ************* Section Nature des Opérations *************

def natOps(request):
    natOp = Natoperation.objects.all()
    context={'values' : natOp}
    return render(request, folderLocation+'index/natOp.html', context)

@csrf_exempt
def natOpCreate(request):
    if request.method == 'POST':
        creerNatOp = natOpForm(request.POST)
        if creerNatOp.is_valid():
            creerNatOp.save()
            return redirect('natOps')
    else:
        creerNatOp = natOpForm()
    context={'creerNatOp' : creerNatOp}
    return render(request, folderLocation+'create/natOpCreate.html', context)

@csrf_exempt
def natOpEdit(request, pk):
    natOp = get_object_or_404(Natoperation, idnatope=pk)
    modifierNatOp = natOpForm(request.POST or None, instance=natOp)
    if modifierNatOp.is_valid():
        modifierNatOp.save()
        return redirect('natOps')
    context = {'modifierNatOp': modifierNatOp}
    return render(request, folderLocation+'edit/natOpEdit.html', context)

@csrf_exempt
def natOpInfo(request, pk):
    natOp = Natoperation.objects.get(idnatope=pk)
    infoNatOp = natOpForm(request.POST or None, instance=natOp)
    context = {'infoNatOp': infoNatOp}
    return render(request, folderLocation+'info/natOpInfo.html', context)

@csrf_exempt
def natOpDelete(request, pk):
    natOp = get_object_or_404(Natoperation, idnatope=pk)
    if request.method == 'POST':
        natOp.delete()
        return redirect('natOps')
    context = {'natOp': natOp}
    return render(request, folderLocation+'delete/natOpDelete.html', context)


