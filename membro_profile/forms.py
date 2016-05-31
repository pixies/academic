#-*- encoding: utf-8 -*-
from membro_profile.models import MembroProfile
from django.contrib.auth.models import User
from django import forms

class MembroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email','password')

class MembroProfileForm(forms.ModelForm):
    class Meta:
        model = MembroProfile
        fields = ('cpf','tipo_de_inscricao','avatar')

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    cpf = forms.CharField(label="CPF")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cpf')