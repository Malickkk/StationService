from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import json

from .models import *
from .forms import *

# Create your views here.

folderLocation = 'interfaces/administ/parametreDeBase/'

def index(request):
    context={}
    return render(request, 'interfaces/administ/mainIndex.html', context)

def indexAdmin(request):
    interface="Administrateur"
    context={'interface':interface}
    return render(request, 'interfaces/administ/indexAdmin.html', context)

def indexGerant(request):
    interface="Gerant"
    context={'interface':interface}
    return render(request, 'interfaces/gerant/indexGerant.html', context)

def indexAgent(request):
    interface="Agent"
    context={'interface':interface}
    return render(request, 'interfaces/agent/indexAgent.html', context)

# REDIRECT TO A NEW LOCATION
class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['HX-Redirect']=self['Location']
    status_code = 200

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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("stationServices"))

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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("stationServices"))

    context = {'modifierStation': modifierStation}
    return render(request, folderLocation+'edit/stationEdit.html', context)

@csrf_exempt
def stationInfo(request, pk):
    station = get_object_or_404(Stationservice, idstation=pk)
    infoStation = stationServiceForm(request.POST or None, instance=station)
    context = {'infoStation': infoStation}
    return render(request, folderLocation+'info/stationInfo.html', context)

@csrf_exempt
def stationDelete(request, pk):
    station = get_object_or_404(Stationservice, idstation=pk)
    if request.method == 'POST':
        station.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("stationServices"))
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("users"))
    else:
        creerUserForm = utilisateurForm()
    context={'creerUserForm' : creerUserForm}
    return render(request, folderLocation+'create/userCreate.html', context)

@csrf_exempt
def userEdit(request, pk):
    user = get_object_or_404(Utilisateur, iduser=pk)
    if request.method == "POST":
        modifierUser = utilisateurForm(request.POST or None, instance=user)
        if modifierUser.is_valid():
            modifierUser.save()
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("users"))
    else:
        modifierUser = utilisateurForm(instance=user)
    context = {'modifierUser': modifierUser, 'user':user}
    return render(request, folderLocation+'edit/userEdit.html', context)

@csrf_exempt
def userInfo(request, pk):
    user = get_object_or_404(Utilisateur, iduser=pk)
    infoUser = utilisateurForm(instance=user)
    context = {'infoUser': infoUser}
    return render(request, folderLocation+'info/userInfo.html', context)

@csrf_exempt
def userDelete(request, pk):
    user = get_object_or_404(Utilisateur, iduser=pk)
    if request.method == 'POST':
        user.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("users"))
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
        creerarticleForm = articleForm(request.POST)
        if creerarticleForm.is_valid():
            creerarticleForm.save()
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("articles"))
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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("articles"))
    context = {'modifierarticle': modifierarticle}
    return render(request, folderLocation+'edit/articleEdit.html', context)

@csrf_exempt
def articleInfo(request, pk):
    article = get_object_or_404(Article, idarticle=pk)
    infoarticle = articleForm(request.POST or None, instance=article)
    context = {'infoarticle': infoarticle}
    return render(request, folderLocation+'info/articleInfo.html', context)

@csrf_exempt
def articleDelete(request, pk):
    article = get_object_or_404(Article, idarticle=pk)
    if request.method == 'POST':
        article.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("articles"))
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifs"))
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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifs"))
    context = {'modifierTarif': modifierTarif}
    return render(request, folderLocation+'edit/tarifEdit.html', context)

@csrf_exempt
def tarifInfo(request, pk):
    tarif = get_object_or_404(Tarif, idtarif=pk)
    infoTarif = tarifForm(request.POST or None, instance=tarif)
    print(tarif.datedebut - tarif.datefin)
    context = {'infoTarif': infoTarif}
    return render(request, folderLocation+'info/tarifInfo.html', context)

@csrf_exempt
def tarifDelete(request, pk):
    tarif = get_object_or_404(Tarif, idtarif=pk)
    if request.method == 'POST':
        tarif.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifs"))
    context = {'tarif': tarif}
    return render(request, folderLocation+'delete/tarifDelete.html', context)


# ************* Section Famille articles *************

def familleArticles(request):
    familleArticles = FamilleArticle.objects.all()
    context={'values' : familleArticles}
    return render(request, folderLocation+'index/familleArticles.html', context)

@csrf_exempt
def familleArticleCreate(request):
    if request.method == 'POST':
        creerfamilleArticleForm = familleArticleForm(request.POST)
        if creerfamilleArticleForm.is_valid():
            creerfamilleArticleForm.save()
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("familleArticles"))
    else:
        creerfamilleArticleForm = familleArticleForm()
    context={'creerfamilleArticleForm' : creerfamilleArticleForm}
    return render(request, folderLocation+'create/familleArticleCreate.html', context)

@csrf_exempt
def familleArticleEdit(request, pk):
    familleArticle = get_object_or_404(FamilleArticle, idfamille=pk)
    modifierfamilleArticle = familleArticleForm(request.POST or None, instance=familleArticle)
    if modifierfamilleArticle.is_valid():
        modifierfamilleArticle.save()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("familleArticles"))
    context = {'modifierfamilleArticle': modifierfamilleArticle}
    return render(request, folderLocation+'edit/familleArticleEdit.html', context)

@csrf_exempt
def familleArticleInfo(request, pk):
    familleArticle = get_object_or_404(FamilleArticle, idfamille=pk)
    infofamilleArticle = familleArticleForm(request.POST or None, instance=familleArticle)
    context = {'infofamilleArticle': infofamilleArticle}
    return render(request, folderLocation+'info/familleArticleInfo.html', context)

@csrf_exempt
def familleArticleDelete(request, pk):
    familleArticle = get_object_or_404(FamilleArticle, idfamille=pk)
    if request.method == 'POST':
        familleArticle.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("familleArticles"))
    context = {'familleArticle': familleArticle}
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("clients"))
    else:
        creerClient = clientForm()
    context={'creerClient' : creerClient}
    return render(request, folderLocation+'create/clientCreate.html', context)

@csrf_exempt
def clientEdit(request, pk):
    client = get_object_or_404(Client, idcli=pk)
    modifierClient = clientForm(request.POST or None, instance=client)
    if modifierClient.is_valid():
        modifierClient.save()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("clients"))
    context = {'modifierClient': modifierClient}
    return render(request, folderLocation+'edit/clientEdit.html', context)

@csrf_exempt
def clientInfo(request, pk):
    client = Client.objects.get(idcli=pk)
    infoClient = clientForm(request.POST or None, instance=client)
    context = {'infoClient': infoClient}
    return render(request, folderLocation+'info/clientInfo.html', context)

@csrf_exempt
def clientDelete(request, pk):
    client = get_object_or_404(Client, idcli=pk)
    if request.method == 'POST':
        client.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("clients"))
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifClient"))
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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifClient"))
    context = {'modifierTarifClient': modifierTarifClient}
    return render(request, folderLocation+'edit/tarifClientEdit.html', context)

@csrf_exempt
def tarifClientInfo(request, pk):
    tarifClient = get_object_or_404(TarifsClient, idtarcli=pk)
    infoTarifClient = tarifClientForm(request.POST or None, instance=tarifClient)
    context = {'infoTarifClient': infoTarifClient}
    return render(request, folderLocation+'info/tarifClientInfo.html', context)

@csrf_exempt
def tarifClientDelete(request, pk):
    tarifClient = get_object_or_404(TarifsClient, idtarcli=pk)
    if request.method == 'POST':
        tarifClient.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifClient"))
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("fournisseurs"))
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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("fournisseurs"))
    context = {'modifierFournisseur': modifierFournisseur}
    return render(request, folderLocation+'edit/fournisseurEdit.html', context)

@csrf_exempt
def fournisseurInfo(request, pk):
    fournisseur = get_object_or_404(Fournisseur, idfourn=pk)
    infoFournisseur = fournForm(request.POST or None, instance=fournisseur)
    context = {'infoFournisseur': infoFournisseur}
    return render(request, folderLocation+'info/fournisseurInfo.html', context)

@csrf_exempt
def fournisseurDelete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, idfourn=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("fournisseurs"))
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifFournisseur"))
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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifFournisseur"))
    context = {'modifierTarifFournisseur': modifierTarifFournisseur}
    return render(request, folderLocation+'edit/tarifFournisseurEdit.html', context)

@csrf_exempt
def tarifFournisseurInfo(request, pk):
    tarifFournisseur = get_object_or_404(Tarifsfourn, idtarfourn=pk)
    infoTarifFournisseur = tarifFournForm(request.POST or None, instance=tarifFournisseur)
    context = {'infoTarifFournisseur': infoTarifFournisseur}
    return render(request, folderLocation+'info/tarifFournisseurInfo.html', context)

@csrf_exempt
def tarifFournisseurDelete(request, pk):
    tarifFournisseur = get_object_or_404(Tarifsfourn, idtarfourn=pk)
    if request.method == 'POST':
        tarifFournisseur.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("tarifFournisseur"))
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
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("natOps"))
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
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("natOps"))
    context = {'modifierNatOp': modifierNatOp}
    return render(request, folderLocation+'edit/natOpEdit.html', context)

@csrf_exempt
def natOpInfo(request, pk):
    natOp = get_object_or_404(Natoperation, idnatope=pk)
    infoNatOp = natOpForm(request.POST or None, instance=natOp)
    context = {'infoNatOp': infoNatOp}
    return render(request, folderLocation+'info/natOpInfo.html', context)

@csrf_exempt
def natOpDelete(request, pk):
    natOp = get_object_or_404(Natoperation, idnatope=pk)
    if request.method == 'POST':
        natOp.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("natOps"))
    context = {'natOp': natOp}
    return render(request, folderLocation+'delete/natOpDelete.html', context)


# ************* Section Cuve *************

def cuves(request):
    cuve = Cuve.objects.all()
    context={'values' : cuve}
    return render(request, folderLocation+'index/cuve.html', context)

@csrf_exempt
def cuveCreate(request):
    if request.method == 'POST':
        creerCuve = cuveForm(request.POST)
        if creerCuve.is_valid():
            creerCuve.save()
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("cuves"))
    else:
        creerCuve = cuveForm()
    context={'creerCuve' : creerCuve}
    return render(request, folderLocation+'create/cuveCreate.html', context)

@csrf_exempt
def cuveEdit(request, pk):
    cuve = get_object_or_404(Cuve, idcuve=pk)
    modifierCuve = cuveForm(request.POST or None, instance=cuve)
    if modifierCuve.is_valid():
        modifierCuve.save()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("cuves"))
    context = {'modifierCuve': modifierCuve}
    return render(request, folderLocation+'edit/cuveEdit.html', context)

@csrf_exempt
def cuveInfo(request, pk):
    cuve = get_object_or_404(Cuve, idcuve=pk)
    infoCuve = cuveForm(request.POST or None, instance=cuve)
    context = {'infoCuve': infoCuve}
    return render(request, folderLocation+'info/cuveInfo.html', context)

@csrf_exempt
def cuveDelete(request, pk):
    cuve = get_object_or_404(Cuve, idcuve=pk)
    if request.method == 'POST':
        cuve.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("cuves"))
    context = {'cuve': cuve}
    return render(request, folderLocation+'delete/cuveDelete.html', context)


# ************* Section Pompe Cuve *************

def pompes(request):
    pompe = Pompecuve.objects.all()
    context={'values' : pompe}
    return render(request, folderLocation+'index/pompe.html', context)

@csrf_exempt
def pompeCreate(request):
    if request.method == 'POST':
        creerPompe = pompeForm(request.POST)
        if creerPompe.is_valid():
            creerPompe.save()
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("pompes"))
    else:
        creerPompe = pompeForm()
    context={'creerPompe' : creerPompe}
    return render(request, folderLocation+'create/pompeCreate.html', context)

@csrf_exempt
def pompeEdit(request, pk):
    pompe = get_object_or_404(Pompecuve, idpompe=pk)
    modifierPompe = pompeForm(request.POST or None, instance=pompe)
    if modifierPompe.is_valid():
        modifierPompe.save()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("pompes"))
    context = {'modifierPompe': modifierPompe}
    return render(request, folderLocation+'edit/pompeEdit.html', context)

@csrf_exempt
def pompeInfo(request, pk):
    pompe = get_object_or_404(Pompecuve, idpompe=pk)
    infoPompe = pompeForm(request.POST or None, instance=pompe)
    context = {'infoPompe': infoPompe}
    return render(request, folderLocation+'info/pompeInfo.html', context)

@csrf_exempt
def pompeDelete(request, pk):
    pompe = get_object_or_404(Pompecuve, idpompe=pk)
    if request.method == 'POST':
        pompe.delete()
        return HTTPResponseHXRedirect(redirect_to=reverse_lazy("pompes"))
    context = {'pompe': pompe}
    return render(request, folderLocation+'delete/pompeDelete.html', context)