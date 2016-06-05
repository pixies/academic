#-*- encoding: utf-8 -*-
from membro_profile.models import MembroProfile
from django.contrib.auth.models import User
from django import forms

class MembroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email','password')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex.: Fulano de Tau'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex.: da Silva Sauro'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ex.: fulanodetau'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
            #'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        }


class MembroProfileForm(forms.ModelForm):
    class Meta:
        model = MembroProfile
        fields = ('cpf','tipo_de_inscricao','avatar')

        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'Use apenas números.'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
        }

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Primeiro nome")
    last_name = forms.CharField(label="Segundo nome")
    cpf = forms.CharField(label="CPF")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cpf')