from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


PROFIL_USER = (
    (1, 'AGENT'),
    (2, 'GERANT'),
    (3, 'ADMIN FONCTIONNEL'),
    (4, 'ADMIN TECHNIQUE')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'E-mail', 'id':'user'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Mot de passe', 'id':'motdepasse'}
    ))
    station_service = forms.ChoiceField(choices=PROFIL_USER)


# class LivraisonForm(forms.ModelForm):
#     class Meta:
#         model = Entblcarburant
#         fields = "__all__"

# class RegistrationForm(UserCreationForm):
#     # datenaissance = forms.DateField()
#     class Meta:
#         model = Utilisateurs
#         fields = "__all__"
#         # widget = {
#         #     'datenaissance' : DateInput()
#         # }
#     email = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'form-control, form-control-user',
#         'placeholder':'E-mail', 'id':'user'}
#     ))
#     first_name = forms.Field(widget=forms.TextInput(attrs={
#         'class': 'form-control, form-control-user',
#         'placeholder': 'Prénom',
#         }))
#     last_name = forms.Field(widget=forms.TextInput(attrs={
#         'class': 'form-control, form-control-user',
#         'placeholder': 'Nom',
#     }))
#     datenaissance = forms.DateField()

#     password1 = forms.Field(widget=forms.PasswordInput(attrs={
#         'class': 'form-control, form-control-user',
#         'placeholder': 'Mot de passe',
#     }))
#     password2 = forms.Field(widget=forms.PasswordInput(attrs={
#         'class': 'form-control, form-control-user',
#         'placeholder': 'Confirmer le Mot de passe',
#     }))
