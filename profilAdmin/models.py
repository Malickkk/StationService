# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the model, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField


class Utilisateur(models.Model):
    iduser = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    dob = models.DateField()
    # motdepass = models.CharField(max_length=20)
    profiluser = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'utilisateurs'
        

    def __str__(self) -> str:
        return str(self.nom + " " + self.prenom)


class Stationservice(models.Model):
    idstation = models.AutoField(primary_key=True)
    codstation = models.CharField(unique=True, max_length=10)
    pays = CountryField()
    ville = models.CharField(max_length=100)
    adrgeo = models.CharField(max_length=255)
    iduser = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, db_column='iduser')
    telresp1 = models.CharField(max_length=40)
    telresp2 = models.CharField(max_length=40)
    nbdecuve = models.IntegerField()
    nbdepompe = models.IntegerField()
    capcuve = models.IntegerField()
    jourcpta = models.DateField()
    exocpta = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'stationservices'
        

    def __str__(self):
        return 'Station ' + self.codstation


class Natoperation(models.Model): #vente de carburant

    idnatope = models.AutoField(primary_key=True)
    codope = models.CharField(max_length=20, unique=True)
    libope = models.CharField(max_length=40)
    saiqte = models.BooleanField( )
    saival = models.BooleanField( )

    class Meta:
        managed = True
        db_table = 'natoperation'
        

    
    def __str__(self):
        return self.libope


class FamilleArticle(models.Model):
    idfamille = models.AutoField(primary_key=True)
    codfamille = models.CharField(unique=True, max_length=10)
    nomfamille = models.CharField(max_length=40)
    idnatoperation = models.ForeignKey(Natoperation, on_delete=models.CASCADE, db_column='idnatoperation')

    class Meta:
        managed = True
        db_table = 'FamilleArticle'

    def __str__(self):
        return self.nomfamille
        

class Article(models.Model):
    idarticle = models.AutoField(primary_key=True)
    codArticle = models.CharField(db_column='CodArticle', max_length=10, unique=True)  # Field name made lowercase.
    nomArticle = models.CharField(max_length=40)
    idfamille = models.ForeignKey(FamilleArticle, on_delete=models.CASCADE, db_column='idfamille')

    class Meta:
        managed = True
        db_table = 'articles'
        
    
    def __str__(self):
        return self.nomArticle


class Cuve(models.Model):
    idcuve = models.AutoField(primary_key=True)
    codecuve = models.CharField(unique=True, max_length=10)
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    nomcuve = models.CharField(max_length=40)
    capcuve = models.IntegerField( )
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')

    class Meta:
        managed = True
        db_table = 'cuves'


class Client(models.Model):# ajouter: raison sociale 
    idcli = models.AutoField(primary_key=True)
    codcli = models.CharField(unique=True, max_length=10)
    raisonsoc = models.CharField(max_length=255)
    pays = CountryField( )
    ville = models.CharField(max_length=100)
    adrgeo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telresp1 = models.CharField(max_length=40)
    telresp2 = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'clients'
        

    def __str__(self):
        return self.raisonsoc


class Ctrcaisse(models.Model):
    idctrcaisse = models.AutoField(primary_key=True)
    codcaisse = models.CharField(max_length=20, unique=True)
    typctr = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'ctrcaisse'
        

class Bilanjournalier(models.Model):
    idbilan = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idjournee = models.IntegerField( )
    idligbilan = models.IntegerField( )
    datevalidation = models.DateField( )
    iduser = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, db_column='iduser')
    comment = models.CharField(db_column='Comment', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bilanjournalier'
        

class Detblcarburant(models.Model):
    iddetblcar = models.AutoField(primary_key=True)
    identblcar = models.IntegerField( )
    idcuve = models.ForeignKey(Cuve, on_delete=models.CASCADE, db_column='idcuve')
    qtedetliv = models.IntegerField( )
    mondetliv = models.IntegerField( )
    remarkdet = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'detblcarburant'


class Detblgaz(models.Model):
    iddetblgaz = models.AutoField(primary_key=True)
    identblgaz = models.IntegerField( )
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    qtedetliv = models.IntegerField( )
    mondetliv = models.IntegerField( )
    remarkdet = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'detblgaz'


class Detbllub(models.Model):
    iddetbllub = models.AutoField(primary_key=True)
    identbllub = models.IntegerField( )
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    qtedetliv = models.IntegerField( )
    mondetliv = models.IntegerField( )
    remarkdet = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'detbllub'


class Fournisseur(models.Model):
    idfourn = models.AutoField(primary_key=True)
    codfourn = models.CharField(unique=True, max_length=10)
    raisonsoc = models.CharField(max_length=255)
    pays = CountryField( )
    ville = models.CharField(max_length=100)
    adrgeo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telresp1 = models.CharField(max_length=40)
    telresp2 = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'fournisseurs'
        

    def __str__(self):
        return self.raisonsoc


class Journeescomptable(models.Model):
    idjournee = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    datecomptable = models.DateField( )
    joursts = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'journeescomptables'
        

class Entblcarburant(models.Model):
    identblcar = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    idjournee = models.IntegerField( )
    datemvt = models.DateField( )
    numbl = models.CharField(max_length=20)
    qtelivree = models.IntegerField( )
    monlivre = models.IntegerField( )
    prixachat = models.IntegerField()
    idfourn = models.IntegerField( )
    comment = models.CharField(max_length=255)
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'entblcarburant'

        
class Entblgaz(models.Model):
    identblgaz = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    numbl = models.CharField(max_length=20)
    qtelivree = models.IntegerField( )
    monlivre = models.IntegerField( )
    idfourn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, db_column='idfourn')
    comment = models.CharField(max_length=255)
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'entblgaz'


class Entbllub(models.Model):
    identbllub = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    numbl = models.CharField(max_length=20)
    qtelivree = models.IntegerField( )
    monlivre = models.IntegerField( )
    idfourn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, db_column='idfourn')
    comment = models.CharField(max_length=255)
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'entbllub'


class Lignebilan(models.Model):
    idligbilan = models.AutoField(primary_key=True)
    codlign = models.CharField(max_length=10, unique=True)
    libbilan = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'lignebilan'


class Mvtpompecarburant(models.Model):
    idmvtpompe = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idcuve = models.ForeignKey(Cuve, on_delete=models.CASCADE, db_column='idcuve')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    idpompe = models.IntegerField( )
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    indexfermeture = models.IntegerField( )
    indexouverture = models.IntegerField()
    indexdiff = models.IntegerField( )
    remcuve = models.IntegerField( )
    vteqtejour = models.IntegerField( )
    prixdulitre = models.IntegerField( )
    recettejour = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'mvtpompecarburant'


class Mvtscaisse(models.Model):
    idmvtcaisse = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    idnatope = models.ForeignKey(Natoperation, on_delete=models.CASCADE, db_column='idnatope')
    contrpart = models.CharField(max_length=10)
    libope = models.CharField(max_length=40)
    numpiece = models.CharField(max_length=20)
    quantite = models.IntegerField( )
    prixuntaire = models.IntegerField( )
    mtdepense = models.IntegerField( )
    mtrecette = models.IntegerField( )
    comment = models.CharField(max_length=255)
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'mvtscaisse'


class Mvtsclient(models.Model):
    idmvtcli = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idcli = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='idcli')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    soldejm1 = models.IntegerField( )
    mntcrjour = models.IntegerField( )
    mntregjour = models.IntegerField( )
    mntotalcr = models.IntegerField(db_column='Mntotalcr')  # Field name made lowercase.
    mntotalreg = models.IntegerField(db_column='Mntotalreg')  # Field name made lowercase.
    soldejour = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'mvtsclients'


class Mvtsgaz(models.Model):
    idmvtgaz = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    qtestktheojm1 = models.IntegerField( )
    field_valstktheojm1 = models.IntegerField(db_column=' valstktheojm1')
    field_vteqterechgjm1 = models.IntegerField(db_column=' vteqterechgjm1')
    vtevalrechgjm1 = models.IntegerField( )
    vteqteconsgjm1 = models.IntegerField( )
    vtevalconsgjm1 = models.IntegerField( )
    field_qteentreejour = models.IntegerField(db_column=' qteentreejour')
    valentreejour = models.IntegerField( )
    prixunachat = models.IntegerField( )
    qtevterechgjour = models.IntegerField( )
    valvterechgjour = models.IntegerField( )
    prixunvterechg = models.IntegerField( )
    qtestkfinal = models.IntegerField( )
    valstkfinal = models.IntegerField( )
    qtevteconsgjour = models.IntegerField( )
    valvteconsgjour = models.IntegerField( )
    prixunvteconsg = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'mvtsgaz'


class Mvtsodiverse(models.Model):
    idmvtod = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    numveh = models.CharField(max_length=30)
    field_quantite = models.IntegerField(db_column='  quantite')
    field_prixunitaire = models.IntegerField(db_column=' prixunitaire')
    montant = models.IntegerField( )
    comment = models.CharField(max_length=255)
    modpai = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'mvtsodiverses'


class Natopecaisse(models.Model):
    idnatopecaisse = models.AutoField(primary_key=True)
    idctrcaisse = models.ForeignKey(Ctrcaisse, on_delete=models.CASCADE, db_column='idctrcaisse')
    idnatope = models.ForeignKey(Natoperation, on_delete=models.CASCADE, db_column='idnatope')

    class Meta:
        managed = True
        db_table = 'natopecaisse'


class Pompecuve(models.Model):
    idpompe = models.IntegerField( )
    codpompe = models.CharField(unique=True, max_length=10)
    descrpompe = models.CharField(max_length=40)
    idcuve = models.ForeignKey(Cuve, on_delete=models.CASCADE, db_column='idcuve')
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')

    class Meta:
        managed = True
        db_table = 'pompecuve'


class Regclient(models.Model):
    idregcli = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idcli = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='idcli')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    montant = models.IntegerField( )
    modreg = models.IntegerField( )
    numchq = models.CharField(max_length=20)
    numtel = models.CharField(max_length=20)
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'regclients'


class StatArticle(models.Model):
    idstatart = models.AutoField(primary_key=True)
    idfamille = models.ForeignKey(FamilleArticle, on_delete=models.CASCADE, db_column='idfamille')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    periode = models.IntegerField( )
    qteachat = models.IntegerField( )
    mntachat = models.IntegerField( )
    qtevente = models.IntegerField( )
    mntvente = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'statArticles'


class Stockcarburant(models.Model):
    idstck = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idcuve = models.ForeignKey(Cuve, on_delete=models.CASCADE, db_column='idcuve')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    qtestktheojm1 = models.IntegerField( )
    field_valstktheojm1 = models.IntegerField(db_column=' valstktheojm1')
    field_qteentreejour = models.IntegerField(db_column=' qteentreejour')
    valentreejour = models.IntegerField( )
    totatestkcuve = models.IntegerField( )
    totvalstkcuve = models.IntegerField( )
    vteqtejour = models.IntegerField( )
    vtevaljour = models.IntegerField( )
    qtestktheojour = models.IntegerField( )
    valstktheojour = models.IntegerField( )
    qtestkreeljour = models.IntegerField( )
    valstkreeljour = models.IntegerField( )
    diffqtestk = models.IntegerField( )
    diffvalstk = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'stockcarburant'


class Stocklubacc(models.Model):
    idstklub = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    qtestktheojm1 = models.IntegerField( )
    field_valstktheojm1 = models.IntegerField(db_column=' valstktheojm1')
    vteqtejm1 = models.IntegerField( )
    vtevaljm1 = models.IntegerField( )
    field_qteentreejour = models.IntegerField(db_column=' qteentreejour')
    valentreejour = models.IntegerField( )
    prixunachat = models.IntegerField( )
    qtestkfinal = models.IntegerField( )
    valstkfinal = models.IntegerField( )
    qtevtetotal = models.IntegerField( )
    valvtetotal = models.IntegerField( )
    qtevtejour = models.IntegerField( )
    valvtejour = models.IntegerField( )
    prixunvte = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'stocklubacc'


class Tarif(models.Model):
    idtarif = models.AutoField(primary_key=True)
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    datedebut = models.DateField( )
    datefin = models.DateField( )
    monttarif = models.FloatField( )

    class Meta:
        managed = True
        db_table = 'tarifs'
        

    def __str__(self):
        return self.idarticle.nomArticle


class TarifsClient(models.Model):
    idtarcli = models.AutoField(primary_key=True)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='idcli')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    datedebut = models.DateField( )
    datefin = models.DateField( )
    monttarif = models.FloatField( )

    class Meta:
        managed = True
        db_table = 'tarifsclient'
        

    def __str__(self):
        return self.clients.codcli + ' - ' + str(self.monttarif)


class Tarifsfourn(models.Model):
    idtarfourn = models.AutoField(primary_key=True)
    idfourn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, db_column='idfourn')
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    datedebut = models.DateField( )
    datefin = models.DateField( )
    monttarif = models.FloatField( )

    class Meta:
        managed = True
        db_table = 'tarifsfourn'
        


    def __str__(self):
        return self.idfourn.raisonsoc


class Tarifsgaz(models.Model):
    idtarifgaz = models.AutoField(primary_key=True)
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    datedebut = models.DateField( )
    datefin = models.DateField( )
    tarifrchg = models.IntegerField( )
    tarifcsg = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'tarifsgaz'


class Userstation(models.Model):
    iduserstation = models.AutoField(primary_key=True)
    iduser = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, db_column='iduser')
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')

    class Meta:
        managed = True
        db_table = 'userstation'


class Vtesclientcredit(models.Model):
    idvtecli = models.AutoField(primary_key=True)
    idstation = models.ForeignKey(Stationservice, on_delete=models.CASCADE, db_column='idstation')
    idcli = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='idcli')
    idjournee = models.ForeignKey(Journeescomptable, on_delete=models.CASCADE, db_column='idjournee')
    datemvt = models.DateField( )
    idarticle = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='idarticle')
    quantite = models.IntegerField( )
    prixunitaire = models.IntegerField( )
    montant = models.IntegerField( )
    exocpta = models.IntegerField( )

    class Meta:
        managed = True
        db_table = 'vtesclientcredit'