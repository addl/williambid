from back_office.models import TipoMembresia

__author__ = 'bryan'

from django import forms
import re, os
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# class RetoForm(forms.ModelForm):
# #    tipo_reto = forms.Select(choices=reto_choices)
#     personas = forms.IntegerField()
#     mems = TipoMembresia.objects.all()
#     membresia = forms.Select(choices=mems)
#     tiempo = forms.DateTimeField()
#     pujas = forms.FloatField()
#     dinero = forms.FloatField()

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())
    # datos del perfil
    direccion = forms.CharField(label='Direccion', required=False)
    ciudad = forms.CharField(label='Ciudad', required=False)
    provincia = forms.CharField(label='Provincia', required=False)
    pais = forms.CharField(label='Pais', required=False)
    telefono = forms.CharField(label='Telefono', required=False)
    seudonimo = forms.CharField(label='Seudonimo', required=False)
    whatsapp_id = forms.CharField(label='Id de Whatsapp', required=False)
    skype_id = forms.CharField(label='ID de Skype', required=False)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')