from django.shortcuts import render
from django.contrib.staticfiles import finders
from django.shortcuts import render
# Create your views here.

def home(request, *args, **kwargs):
    home_css_path = finders.find('main_site/css/home.css')
    template_path = 'main_site/home.html'

    context = {
        "projetos": [
            {"titulo": "TituloA", "descricao": "DescriacoA"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
            {"titulo": "TituloB", "descricao": "DescriacoB"},
        ]
    }

    return render(request, template_path, context=context)

