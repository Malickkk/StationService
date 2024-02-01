from django.urls import path
from django.contrib.auth import views as auth_views
from users.forms import UserLoginForm


from . import views

urlpatterns = [
    path('connexion/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=UserLoginForm ), 
    name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='deconnexion'),
    path('enregistrement/', views.enregistrement, name='enregistrement'),
    path('indexAgent/', views.indexAgent, name='indexAgent'),
    path('livraisonCarburant/', views.livraisonCarburant, name='livraisonCarburant'),
    path('creerLivraison/', views.creerLivraison, name='creerLivraison'),
    path('mvtPompes/', views.mvtPompes, name='mvtPompes'),
    path('ctrlStockCarburant/', views.ctrlStockCarburant, name='ctrlStockCarburant'),
]