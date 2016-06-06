
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