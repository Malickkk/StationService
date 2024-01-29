from django.test import TestCase
from .models import *

class UtilisateurTestCase(TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur.objects.create(
            email='test@example.com',
            nom='John',
            prenom='Doe',
            dob='1990-01-01',
            profiluser='Test'
        )

    def test_edit_utilisateur(self):
        self.utilisateur.nom = 'Doe'
        self.utilisateur.save()
        updated_utilisateur = Utilisateur.objects.get(iduser=self.utilisateur.iduser)
        self.assertEqual(updated_utilisateur.nom, 'Doe')

    def test_delete_utilisateur(self):
        utilisateur_count_before_delete = Utilisateur.objects.count()
        self.utilisateur.delete()
        utilisateur_count_after_delete = Utilisateur.objects.count()
        self.assertEqual(utilisateur_count_before_delete - 1, utilisateur_count_after_delete)

class StationserviceTestCase(TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur.objects.create(
            email='test@example.com',
            nom='John',
            prenom='Doe',
            dob='1990-01-01',
            profiluser='Test'
        )

        self.stationservice = Stationservice.objects.create(
            codstation='ABC123',
            pays='US',
            ville='New York',
            adrgeo='123 Street',
            iduser=self.utilisateur,
            telresp1='123456',
            telresp2='789012',
            nbdecuve=5,
            nbdepompe=3,
            capcuve=1000,
            jourcpta='2024-01-01',
            exocpta=1
        )

    def test_edit_stationservice(self):
        self.stationservice.codstation = 'XYZ789'
        self.stationservice.save()
        updated_stationservice = Stationservice.objects.get(idstation=self.stationservice.idstation)
        self.assertEqual(updated_stationservice.codstation, 'XYZ789')

    def test_delete_stationservice(self):
        stationservice_count_before_delete = Stationservice.objects.count()
        self.stationservice.delete()
        stationservice_count_after_delete = Stationservice.objects.count()
        self.assertEqual(stationservice_count_before_delete - 1, stationservice_count_after_delete)


class NatoperationTestCase(TestCase):
    def setUp(self):
        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

    def test_edit_natoperation(self):
        self.natoperation.libope = 'Vente de carburant diesel'
        self.natoperation.save()
        updated_natoperation = Natoperation.objects.get(idnatope=self.natoperation.idnatope)
        self.assertEqual(updated_natoperation.libope, 'Vente de carburant diesel')

    def test_delete_natoperation(self):
        natoperation_count_before_delete = Natoperation.objects.count()
        self.natoperation.delete()
        natoperation_count_after_delete = Natoperation.objects.count()
        self.assertEqual(natoperation_count_before_delete - 1, natoperation_count_after_delete)


class FamilleArticleTestCase(TestCase):
    def setUp(self):
        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

        self.famille_article = FamilleArticle.objects.create(
            codfamille='FAM001',
            nomfamille='Carburants',
            idnatoperation=self.natoperation
        )

    def test_edit_famille_article(self):
        self.famille_article.nomfamille = 'Carburants et Lubrifiants'
        self.famille_article.save()
        updated_famille_article = FamilleArticle.objects.get(idfamille=self.famille_article.idfamille)
        self.assertEqual(updated_famille_article.nomfamille, 'Carburants et Lubrifiants')

    def test_delete_famille_article(self):
        famille_article_count_before_delete = FamilleArticle.objects.count()
        self.famille_article.delete()
        famille_article_count_after_delete = FamilleArticle.objects.count()
        self.assertEqual(famille_article_count_before_delete - 1, famille_article_count_after_delete)

class ArticleTestCase(TestCase):
    def setUp(self):
        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

        self.famille_article = FamilleArticle.objects.create(
            codfamille='FAM001',
            nomfamille='Carburants',
            idnatoperation=self.natoperation
        )

        self.article = Article.objects.create(
            codArticle='ART001',
            nomArticle='Diesel',
            idfamille=self.famille_article
        )

    def test_edit_article(self):
        self.article.nomArticle = 'Diesel Plus'
        self.article.save()
        updated_article = Article.objects.get(idarticle=self.article.idarticle)
        self.assertEqual(updated_article.nomArticle, 'Diesel Plus')

    def test_delete_article(self):
        article_count_before_delete = Article.objects.count()
        self.article.delete()
        article_count_after_delete = Article.objects.count()
        self.assertEqual(article_count_before_delete - 1, article_count_after_delete)

class CuveTestCase(TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur.objects.create(
            email='test@example.com',
            nom='John',
            prenom='Doe',
            dob='1990-01-01',
            profiluser='Test'
        )

        self.stationservice = Stationservice.objects.create(
            codstation='ABC123',
            pays='US',
            ville='New York',
            adrgeo='123 Street',
            iduser=self.utilisateur,
            telresp1='123456',
            telresp2='789012',
            nbdecuve=5,
            nbdepompe=3,
            capcuve=1000,
            jourcpta='2024-01-01',
            exocpta=1
        )

        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

        self.famille_article = FamilleArticle.objects.create(
            codfamille='FAM001',
            nomfamille='Carburants',
            idnatoperation=self.natoperation
        )

        self.article = Article.objects.create(
            codArticle='ART001',
            nomArticle='Diesel',
            idfamille=self.famille_article
        )

        self.cuve = Cuve.objects.create(
            codecuve='C001',
            idarticle=self.article,
            nomcuve='Diesel Cuve 1',
            capcuve=1000,
            idstation=self.stationservice
        )

    def test_edit_cuve(self):
        self.cuve.nomcuve = 'Diesel Cuve 2'
        self.cuve.save()
        updated_cuve = Cuve.objects.get(idcuve=self.cuve.idcuve)
        self.assertEqual(updated_cuve.nomcuve, 'Diesel Cuve 2')

    def test_delete_cuve(self):
        cuve_count_before_delete = Cuve.objects.count()
        self.cuve.delete()
        cuve_count_after_delete = Cuve.objects.count()
        self.assertEqual(cuve_count_before_delete - 1, cuve_count_after_delete)

class ClientTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            codcli='CLI001',
            raisonsoc='Client ABC',
            pays='US',
            ville='New York',
            adrgeo='123 Street',
            email='client@example.com',
            telresp1='1234567890',
            telresp2='0987654321'
        )

    def test_edit_client(self):
        self.client.raisonsoc = 'Client XYZ'
        self.client.save()
        updated_client = Client.objects.get(idcli=self.client.idcli)
        self.assertEqual(updated_client.raisonsoc, 'Client XYZ')

    def test_delete_client(self):
        client_count_before_delete = Client.objects.count()
        self.client.delete()
        client_count_after_delete = Client.objects.count()
        self.assertEqual(client_count_before_delete - 1, client_count_after_delete)


class FournisseurTestCase(TestCase):
    def setUp(self):
        self.fournisseur = Fournisseur.objects.create(
            codfourn='FRN001',
            raisonsoc='Fournisseur XYZ',
            pays='US',
            ville='New York',
            adrgeo='456 Street',
            email='supplier@example.com',
            telresp1='9876543210',
            telresp2='0123456789'
        )

    def test_edit_fournisseur(self):
        self.fournisseur.raisonsoc = 'Fournisseur ABC'
        self.fournisseur.save()
        updated_fournisseur = Fournisseur.objects.get(idfourn=self.fournisseur.idfourn)
        self.assertEqual(updated_fournisseur.raisonsoc, 'Fournisseur ABC')

    def test_delete_fournisseur(self):
        fournisseur_count_before_delete = Fournisseur.objects.count()
        self.fournisseur.delete()
        fournisseur_count_after_delete = Fournisseur.objects.count()
        self.assertEqual(fournisseur_count_before_delete - 1, fournisseur_count_after_delete)


class TarifTestCase(TestCase):
    def setUp(self):
        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

        self.famille_article = FamilleArticle.objects.create(
            codfamille='FAM001',
            nomfamille='Carburants',
            idnatoperation=self.natoperation
        )

        self.article = Article.objects.create(
            codArticle='ART001',
            nomArticle='Diesel',
            idfamille=self.famille_article
        )

        self.tarif = Tarif.objects.create(
            datedebut='2024-01-01',
            datefin='2024-12-31',
            monttarif=10.5,
            idarticle=self.article
        )

    def test_edit_tarif(self):
        self.tarif.monttarif = 12.5
        self.tarif.save()
        updated_tarif = Tarif.objects.get(idtarif=self.tarif.idtarif)
        self.assertEqual(updated_tarif.monttarif, 12.5)

    def test_delete_tarif(self):
        tarif_count_before_delete = Tarif.objects.count()
        self.tarif.delete()
        tarif_count_after_delete = Tarif.objects.count()
        self.assertEqual(tarif_count_before_delete - 1, tarif_count_after_delete)

class TarifsClientTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            codcli='CLI001',
            raisonsoc='Client ABC',
            pays='US',
            ville='New York',
            adrgeo='123 Street',
            email='client@example.com',
            telresp1='1234567890',
            telresp2='0987654321'
        )

        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

        self.famille_article = FamilleArticle.objects.create(
            codfamille='FAM001',
            nomfamille='Carburants',
            idnatoperation=self.natoperation
        )

        self.article = Article.objects.create(
            codArticle='ART001',
            nomArticle='Diesel',
            idfamille=self.famille_article
        )

        self.tarif = Tarif.objects.create(
            datedebut='2024-01-01',
            datefin='2024-12-31',
            monttarif=10.5,
            idarticle=self.article
        )

        self.tarif_client = TarifsClient.objects.create(
            clients=self.client,
            datedebut='2024-01-01',
            datefin='2024-12-31',
            monttarif=10.5,
            idarticle=self.article
        )

    def test_edit_tarif_client(self):
        self.tarif_client.monttarif = 12.5
        self.tarif_client.save()
        updated_tarif_client = TarifsClient.objects.get(idtarcli=self.tarif_client.idtarcli)
        self.assertEqual(updated_tarif_client.monttarif, 12.5)

    def test_delete_tarif_client(self):
        tarif_client_count_before_delete = TarifsClient.objects.count()
        self.tarif_client.delete()
        tarif_client_count_after_delete = TarifsClient.objects.count()
        self.assertEqual(tarif_client_count_before_delete - 1, tarif_client_count_after_delete)


class TarifsfournTestCase(TestCase):
    def setUp(self):
        self.natoperation = Natoperation.objects.create(
            codope='V1',
            libope='Vente de carburant',
            saiqte=True,
            saival=False
        )

        self.famille_article = FamilleArticle.objects.create(
            codfamille='FAM001',
            nomfamille='Carburants',
            idnatoperation=self.natoperation
        )

        self.article = Article.objects.create(
            codArticle='ART001',
            nomArticle='Diesel',
            idfamille=self.famille_article
        )

        self.tarif = Tarif.objects.create(
            datedebut='2024-01-01',
            datefin='2024-12-31',
            monttarif=10.5,
            idarticle=self.article
        )

        self.fournisseur = Fournisseur.objects.create(
            codfourn='FRN001',
            raisonsoc='Fournisseur XYZ',
            pays='US',
            ville='New York',
            adrgeo='456 Street',
            email='supplier@example.com',
            telresp1='9876543210',
            telresp2='0123456789'
        )

        self.tarif_fournisseur = Tarifsfourn.objects.create(
            idfourn=self.fournisseur,
            datedebut='2024-01-01',
            datefin='2024-12-31',
            monttarif=8.5,
            idarticle=self.article
        )

    def test_edit_tarif_fournisseur(self):
        self.tarif_fournisseur.monttarif = 9.5
        self.tarif_fournisseur.save()
        updated_tarif_fournisseur = Tarifsfourn.objects.get(idtarfourn=self.tarif_fournisseur.idtarfourn)
        self.assertEqual(updated_tarif_fournisseur.monttarif, 9.5)

    def test_delete_tarif_fournisseur(self):
        tarif_fournisseur_count_before_delete = Tarifsfourn.objects.count()
        self.tarif_fournisseur.delete()
        tarif_fournisseur_count_after_delete = Tarifsfourn.objects.count()
        self.assertEqual(tarif_fournisseur_count_before_delete - 1, tarif_fournisseur_count_after_delete)