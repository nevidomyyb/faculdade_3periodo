from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        # help_text="Insira o usuário", required=True, label="Insira seu usuário"
        )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput()
        # help_text="Insira sua senha", required=True, label="Insira sua senha"
        )

    