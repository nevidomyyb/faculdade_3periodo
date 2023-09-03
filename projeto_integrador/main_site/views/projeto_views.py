from django.contrib.staticfiles import finders
from django.shortcuts import render
from main_site.models import Projeto
from django.shortcuts import get_object_or_404

def visualizar_projeto(request, pk,*args, **kwargs):
    projeto_obj = get_object_or_404(Projeto, pk=pk)
    template_path = 'main_site/view.html'
   
    context = {
        "projeto": 
            {
                "titulo": projeto_obj.titulo,
                "descricao": projeto_obj.descricao,
                "imagem": projeto_obj.imagem
            }
            
    }
    if projeto_obj.autor == request.user:
        context["projeto"]["autor"] = True
    return render(request, template_path, context)

def editar_projeto(request, pk, *args, **kwargs):
    projeto_obj = get_object_or_404(Projeto, pk=pk)