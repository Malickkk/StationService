from django.urls import path

from . import views

urlpatterns = [

    path('', views.indexAdmin, name='indexAdmin'),
    path('indexAdmin/', views.indexAdmin, name='indexAdmin'),

    # ************* Section StationServices *************
    path('stationServices/', views.stationServices, name='stationServices'),
    path('stationcreate/', views.stationCreate, name='stationcreate'),
    path('stationedit/<str:pk>', views.stationEdit, name='stationedit'),
    path('stationinfo/<str:pk>', views.stationInfo, name='stationinfo'),
    path('stationdelete/<int:pk>', views.stationDelete, name='stationdelete'),

    # ************* Section Utilisateurs *************
    path('users/', views.users, name='users'),
    path('usercreate/', views.userCreate, name='usercreate'),
    path('useredit/<str:pk>', views.userEdit, name='useredit'),
    path('userinfo/<str:pk>', views.userInfo, name='userinfo'),
    path('userdelete/<int:pk>', views.userDelete, name='userdelete'),

    # ************* Section Articles *************
    path('articles/', views.articles, name='articles'),
    path('articlecreate/', views.creerArticle, name='articlecreate'),
    path('articleedit/<str:pk>', views.articleEdit, name='articleedit'),
    path('articleinfo/<str:pk>', views.articleInfo, name='articleinfo'),
    path('articledelete/<int:pk>', views.articleDelete, name='articledelete'),
    
    # ************* Section Tarifs *************
    path('tarifs/', views.tarifs, name='tarifs'),
    path('tarifcreate/', views.tarifCreate, name='tarifcreate'),
    path('tarifedit/<str:pk>', views.tarifEdit, name='tarifedit'),
    path('tarifinfo/<str:pk>', views.tarifInfo, name='tarifinfo'),
    path('tarifdelete/<int:pk>', views.tarifDelete, name='tarifdelete'),

    # ************* Section Client *************
    path('client/', views.clients, name='clients'),
    path('clientcreate/', views.clientCreate, name='clientcreate'),
    path('clientedit/<str:pk>', views.clientEdit, name='clientedit'),
    path('clientinfo/<str:pk>', views.clientInfo, name='clientinfo'),
    path('clientdelete/<int:pk>', views.clientDelete, name='clientdelete'),

    # ************* Section Tarif Client *************
    path('tarifClient/', views.tarifClient, name='tarifClient'),
    path('tarifClientCreate/', views.tarifClientCreate, name='tarifclientcreate'),
    path('tarifClientEdit/<str:pk>', views.tarifClientEdit, name='tarifclientedit'),
    path('tarifClientInfo/<str:pk>', views.tarifClientInfo, name='tarifclientinfo'),
    path('tarifClientDelete/<int:pk>', views.tarifClientDelete, name='tarifclientdelete'),

    # ************* Section Fournisseur *************
    path('fournisseur/', views.fournisseurs, name='fournisseurs'),
    path('fournisseurcreate/', views.fournisseurCreate, name='fournisseurcreate'),
    path('fournisseuredit/<str:pk>', views.fournisseurEdit, name='fournisseuredit'),
    path('fournisseurinfo/<str:pk>', views.fournisseurInfo, name='fournisseurinfo'),
    path('fournisseurdelete/<int:pk>', views.fournisseurDelete, name='fournisseurdelete'),

    # ************* Section Tarif Fournisseur *************
    path('tarifFournisseur/', views.tarifFournisseur, name='tarifFournisseur'),
    path('tarifFournisseurcreate/', views.tarifFournisseurCreate, name='tariffournisseurcreate'),
    path('tarifFournisseuredit/<str:pk>', views.tarifFournisseurEdit, name='tariffournisseuredit'),
    path('tarifFournisseurinfo/<str:pk>', views.tarifFournisseurInfo, name='tariffournisseurinfo'),
    path('tarifFournisseurdelete/<int:pk>', views.tarifFournisseurDelete, name='tariffournisseurdelete'),
 
    # ************* Section Famille Articles *************
    path('familleArticles/', views.familleArticles, name='familleArticles'),
    path('familleArticlecreate/', views.familleArticleCreate, name='familleArticlecreate'),
    path('familleArticleedit/<str:pk>', views.familleArticleEdit, name='familleArticleedit'),
    path('familleArticleinfo/<str:pk>', views.familleArticleInfo, name='familleArticleinfo'),
    path('familleArticledelete/<int:pk>', views.familleArticleDelete, name='familleArticledelete'),

     # ************* Section Nature des Opérations *************
    path('natOps/', views.natOps, name='natOps'),
    path('natOpcreate/', views.natOpCreate, name='natOpcreate'),
    path('natOpedit/<str:pk>', views.natOpEdit, name='natOpedit'),
    path('natOpinfo/<str:pk>', views.natOpInfo, name='natOpinfo'),
    path('natOpdelete/<int:pk>', views.natOpDelete, name='natOpdelete'),
]