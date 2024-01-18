from django import forms

from .models import *

FONCTION_CHOICES = (
    ('Agent', "Agent"),
    ('Gérant', "Gérant"),
    ('Administrateur Fonctionnel', "Administrateur Fonctionnel"),
    ('Administrateur Technique', "Administrateur Technique"),
)

class DateInput(forms.DateInput):
    input_type = 'date'
    
dateInput = DateInput(
                format='%d/%m/%Y',
                attrs={
                'class': 'form-control', 
                })

class stationServiceForm(forms.ModelForm):
    class Meta:
        model = Stationservice
        fields = '__all__'
        labels = {
            'iduser': "Gérant", 
            "idpays": "Pays",
            "idville": "Ville",
            "adrgeo": "Adresse géographique",
            "telresp1": "Telephone responsable 1",
            "telresp2": "Telephone responsable 2",
            "nbdecuve": "Nombre de cuves",
            "nbdepompe": "Nombre de pompes",
            "capcuve": "Capacité de cuve",
            "jourcpta": "Journée comptable",
            "exocpta": "Exercice comptable",
            }
        widgets = {
            'jourcpta': dateInput
        }

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'codArticle': "Code de l'Article", 
            "nomArticle": "Nom de l'Article",
            "idfamille": "Famille de l'Article",
            }


class famillearticleForm(forms.ModelForm):
    class Meta:
        model = Famillearticle
        fields = '__all__'
        labels = {
            'codfamille': "Code famille", 
            "nomfamille": "Description famille",
            "idnatoperation": "Identifiant nature opération",
            }


class tarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = '__all__'
        labels = {
            'idArticle': "Article", 
            "datedebut": "Date de debut de validité",
            "datefin": "Date de fin de validité",
            "monttarif": "Montant",
            }
        widgets = {
            "datedebut": dateInput,
            "datefin": dateInput
        }

class tarifClientForm(forms.ModelForm):
    class Meta:
        model = TarifsClient
        fields = '__all__'
        labels = {
            'idcli' : 'Client',
            'idArticle': "Article", 
            "datedebut": "Date de debut de validité",
            "datefin": "Date de fin de validité",
            "monttarif": "Montant",
            }
        widgets = {
            "datedebut": dateInput,
            "datefin": dateInput
        }


class tarifFournForm(forms.ModelForm):
    class Meta:
        model = Tarifsfourn
        fields = '__all__'
        labels = {
            'idfourn' : 'Fournisseur',
            'idArticle': "Article", 
            "datedebut": "Date de debut de validité",
            "datefin": "Date de fin de validité",
            "monttarif": "Montant",
            }
        widgets = {
            "datedebut": dateInput,
            "datefin": dateInput
        }


class utilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'
        labels = {
            'prenom': "Prénom",
            'profiluser': "Fonction", 
            "dob": "Date de naissance",
        }
        widgets = {
            "dob": dateInput,
            "profiluser" : forms.Select(choices=FONCTION_CHOICES,attrs={'class': 'form-control'})
        }


class natOpForm(forms.ModelForm):
    class Meta:
        model = Natoperation
        fields = ('codope', 'libope')
        labels = {
            'codope':"Code nature opération",
            'libope':"Libellé opération",
            # 'saiqte':"Saisie quantité",
            # 'saival':"Saisie valeur",
        }

class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels ={
            'codcli':"Code client",
            'raisonsoc':"Raison sociale",
            'adrgeo':"Adresse géographique",
            'telresp1':"Téléphone 1",
            'telresp2':"Téléphone 2",
        }


class fournForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'
        labels ={
            'codfourn':"Code fournisseur",
            'raisonsoc':"Raison sociale",
            'adrgeo':"Adresse géographique",
            'telresp1':"Téléphone 1",
            'telresp2':"Téléphone 2",
        }