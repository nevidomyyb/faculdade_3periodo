from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from main_site.forms.login_form import LoginForm
from main_site.forms.register_form import RegisterForm
from django.http import Http404
from django.contrib.auth.models import User

def register(request, *args, **kwargs):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'main_site/login.html', {
        'login': False,
        'form': form,
        'form_action': reverse('main_site:perform_register')
    })

def perform_register(request, *args, **kwargs):
    if not request.POST:
        raise Http404
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    if form.is_valid():
        user = User(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email']
        )
        user.set_password(form.cleaned_data['password'])
        user.save()
        del(request.session['register_form_data'])
        return redirect(reverse('main_site:login'))
    return redirect('main_site:register')

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
        if is_authenticated is not None:
            lg(request, is_authenticated)
            return redirect(reverse("main_site:home"))
    return redirect(reverse('main_site:login'))


@login_required(login_url='main_site:login', redirect_field_name='next')
def logoutAA(request):
    logout(request)
    return redirect(reverse('main_site:home'))
