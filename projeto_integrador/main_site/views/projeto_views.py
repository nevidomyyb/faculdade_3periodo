from django.contrib.staticfiles import finders
from django.shortcuts import render
from main_site.forms.editor_form import EditorForm
from main_site.models import Projeto
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
import os

def visualizar_projeto(request, pk,*args, **kwargs):
    projeto_obj = get_object_or_404(Projeto, pk=pk)
    template_path = 'main_site/view.html'
   
    context = {
        "projeto": 
            {
                "id": projeto_obj.idprojeto,
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
    if  not projeto_obj.autor == request.user: Http404
    edit_form_data = request.session.get('edit_form_data', None)
    template_path = 'main_site/editor.html'
    projeto_obj.imagem = ""
    form = EditorForm(instance=projeto_obj)
    context = {
        "form": form,
        "projeto": 
            {
                "idprojeto": projeto_obj.idprojeto,
                "titulo": projeto_obj.titulo,
                "descricao": projeto_obj.descricao,
            },
        # "form_action": reverse('main_site:performar_editar_projeto')
    }
    return render(request, template_path, context)

def criar_projeto(request, *args, **kwargs):
    template_path = 'main_site/editor.html'
    form = EditorForm(request.session.get('register_form_data', None))
    context = {
        "form": form,
        "criacao": True,
    }
    return render(request, template_path, context)

def performar_criar_projeto(request):

    if not request.POST: Http404
    POST = request.POST
    request.session['register_form_data'] = POST
    form = EditorForm(POST, request.FILES)
    if form.is_valid():
        imagem_enviada = request.FILES.get('imagem', None)
        instance = Projeto(
            autor=request.user,
            titulo=form.cleaned_data['titulo'],
            descricao=form.cleaned_data['descricao'],
            imagem=imagem_enviada
        )
        instance.save()
        del(request.session['register_form_data'])
        return redirect(reverse('main_site:visualizar_projeto', args=[instance.idprojeto]))
    else:
        return redirect(reverse('main_site:criar_projeto'))


def performar_editar_projeto(request, pk, *args, **kwargs):
    projeto_obj = get_object_or_404(Projeto, pk=pk)
    if not projeto_obj.autor == request.user: Http404
    if not request.POST: Http404
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = EditorForm(request.POST, request.FILES, instance=projeto_obj)
    if form.is_valid():
        imagem = request.FILES.get('imagem', None)
        projeto_obj.titulo = form.cleaned_data['titulo']
        projeto_obj.descricao = form.cleaned_data['descricao']
        if imagem:
            projeto_obj.imagem = imagem

        projeto_obj.save()
        del(request.session['register_form_data'])
        return redirect(reverse('main_site:visualizar_projeto', args=[pk]))
    errors = form.errors
    print(errors)
    return redirect(reverse('main_site:visualizar_projeto', args=[pk]))