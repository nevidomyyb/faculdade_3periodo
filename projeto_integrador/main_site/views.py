from django.shortcuts import render
from django.contrib.staticfiles import finders
from django.shortcuts import render
from main_site.models import Projeto
# Create your views here.

def home(request, *args, **kwargs):
    home_css_path = finders.find('main_site/css/home.css')
    template_path = 'main_site/home.html'


    context = {
        "projetos": [
            {"titulo": projeto.titulo, "imagem": "media/"+projeto.imagem.path, "descricao": projeto.descricao[0:len(projeto.descricao)-10]} for projeto in Projeto.objects.all()
        ]
    }

    return render(request, template_path, context=context)

