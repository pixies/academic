#-*- encoding: utf-8 -*-
from submissao.models import Submissao
from django import forms

class SubmissaoForm(forms.ModelForm):

    class Meta:
        model = Submissao
        fields = ('titulo','titulo_eng','resumo','autor','area')


"""
class EditSubmissaoForm(forms.ModelForm):
    first_name = forms.CharField(label="Resumo")
    last_name = forms.ChoiceField(label="Autor")
    cpf = forms.ChoiceField(label="Área de atuação")

    class Meta:
        model = Submissao
        fields = ('resumo', 'autor', 'area')
"""