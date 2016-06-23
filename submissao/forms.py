
from django import forms

from submissao.models import Submissao

class SubmissaoForm(forms.ModelForm):
    class Meta:
        model = Submissao
        fields = [
        'titulo',
        'titulo_eng',
        'arquivo',
        'autor',
        'area_de_interesse'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do Resumo', 'class':'form-control'}),
            'titulo_eng': forms.TextInput(attrs={'placeholder': 'Título do Resumo em Inglês', 'class':'form-control'}),
            #'autor': forms.TextInput(attrs={'type':'hidden', 'value':'cleyton'}),
            #'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        }

