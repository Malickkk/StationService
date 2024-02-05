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
    
dateInput = DateInput(attrs={'class': 'form-control'})

class stationServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(stationServiceForm, self).__init__(*args, **kwargs)
        # ONLY GET THE USER WHO ARE "GERANT"
        self.fields['iduser'].queryset = Utilisateur.objects.filter(profiluser="Gérant")
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # READ ONLY FIELD FOR THE CODE, CANNOT BE EDITED ONCE CREATED
            self.fields['codstation'].widget.attrs['readonly'] = True

    def clean_codstation(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.codstation
        else:
            return self.cleaned_data['codstation']
    class Meta:
        model = Stationservice
        fields = '__all__'
        labels = {
            'iduser': "Gérant", 
            "idpays": "Pays",
            "idville": "Ville",
            "codstation": "Code station",
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
    def __init__(self, *args, **kwargs):
        super(articleForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # READ ONLY FIELD FOR THE CODE, CANNOT BE EDITED ONCE CREATED
            self.fields['codArticle'].widget.attrs['readonly'] = True

    def clean_codArticle(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.codArticle
        else:
            return self.cleaned_data['codArticle']
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'codArticle': "Code de l'Article", 
            "nomArticle": "Nom de l'Article",
            "idfamille": "Famille de l'Article",
            }


class familleArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(familleArticleForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # READ ONLY FIELD FOR THE CODE, CANNOT BE EDITED ONCE CREATED
            self.fields['codfamille'].widget.attrs['readonly'] = True

    def clean_codfamille(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.codfamille
        else:
            return self.cleaned_data['codfamille']
    class Meta:
        model = FamilleArticle
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
    def __init__(self, *args, **kwargs):
        super(natOpForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # READ ONLY FIELD FOR THE CODE, CANNOT BE EDITED ONCE CREATED
            self.fields['codope'].widget.attrs['readonly'] = True

    def clean_codope(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.codope
        else:
            return self.cleaned_data['codope']
    class Meta:
        model = Natoperation
        fields = '__all__'
        labels = {
            'codope':"Code nature opération",
            'libope':"Libellé opération",
            'saiqte':"Saisie quantité",
            'saival':"Saisie valeur",
        }

class clientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(clientForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # READ ONLY FIELD FOR THE CODE, CANNOT BE EDITED ONCE CREATED
            self.fields['codcli'].widget.attrs['readonly'] = True

    def clean_codcli(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.codcli
        else:
            return self.cleaned_data['codcli']
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
    def __init__(self, *args, **kwargs):
        super(Fournisseur, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # READ ONLY FIELD FOR THE CODE, CANNOT BE EDITED ONCE CREATED
            self.fields['codfourn'].widget.attrs['readonly'] = True

    def clean_codfourn(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.codfourn
        else:
            return self.cleaned_data['codfourn']
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