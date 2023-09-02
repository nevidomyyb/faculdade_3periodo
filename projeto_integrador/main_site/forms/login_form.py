from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, new_attr_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {new_attr_val}'.strip()

class LoginForm(forms.Form):
    username = forms.CharField(
         widget=forms.TextInput(attrs={'placeholder': 'Usuário'})
        )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Senha'})
        )
    
    

    