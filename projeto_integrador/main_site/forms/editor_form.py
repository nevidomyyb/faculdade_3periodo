from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from main_site.models import Projeto

class EditorForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem']

    titulo = forms.CharField(
        label='Nome do projeto',
        widget=forms.TextInput()
        
    )
    titulo.widget.attrs.update(
        {
            "placeholder": "Nome do projeto aqui",
        }
    )
    descricao = forms.CharField(
        label='Descrição do projeto',
        widget=forms.Textarea()
        
    )
    descricao.widget.attrs.update(
        {
            "placeholder": "Descrição do projeto aqui",
            "cols": 30,
            "rows": 10
        }
    )

    imagem = forms.ImageField(
        label ="Capa do projeto",
        widget=forms.ClearableFileInput(),
        required= False
    )
    imagem.widget.attrs.update({
        "placeholder": "Selecione a imagem",
        "required": False
    })