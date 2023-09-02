from django.contrib.staticfiles import finders
from django.shortcuts import render
from main_site.models import Projeto
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from main_site.forms.login_form import LoginForm
from django.http import Http404
# Create your views here.

def home(request, *args, **kwargs):
    home_css_path = finders.find('main_site/css/home.css')
    template_path = 'main_site/home.html'
    

    context = {
        "projetos": [
            {"titulo": projeto.titulo, "imagem": "media/"+projeto.imagem.path, "descricao": projeto.descricao[0:len(projeto.descricao)-10]} for projeto in Projeto.objects.all()
        ]
    }
    if request.user.is_authenticated:
        context["usuario_logado"] = request.user.username
    return render(request, template_path, context=context)

def login(request, *args, **kwargs):
    form = LoginForm()
    if (request.user.is_authenticated):
        return redirect(reverse('main_site:home'))
    else:
        return render(request, 'main_site/login.html', {
            'login': True,
            'form': form,
            'form_action': reverse('main_site:auth')
        })
    
def auth(request, *args, **kwargs):
    if not request.POST:
        raise Http404
    form = LoginForm(request.POST)
    if form.is_valid():
        is_authenticated = authenticate(request=request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        print(is_authenticated)
        if is_authenticated is not None:
            lg(request, is_authenticated)
            print("Está autenticado: ",request.user.is_authenticated)
            return redirect(reverse("main_site:home"))
    return redirect(reverse('main_site:login'))


@login_required(login_url='main_site:login', redirect_field_name='next')
def logoutAA(request):
    logout(request)
    return redirect(reverse('main_site:home'))
