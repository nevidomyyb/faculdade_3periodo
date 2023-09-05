from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def add_attr(field, attr_name, new_attr_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {new_attr_val}'.strip()

class RegisterForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Insira o usuário desejado'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Insira o email desejado'})
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Insira a senha desejada'})
    )

    def clean_password(self):
        invalid_chars = ['/', '\\', ';', '`', "'", '"', ':']
        string = ''.join(invalid_chars)
        senha = self.cleaned_data['password']
        for char in senha:
            if char in invalid_chars:
                raise ValidationError(f'Você não pode utilizar: {string} na sua senha.', code='invalid')
        return senha

    def clean_email(self):
        email = self.cleaned_data['email']
        exist = User.objects.filter(email=email).first()
        if exist: 
            raise ValidationError(f'Já existe usuário criado com esse email.', code='invalid')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        exist = User.objects.filter(username=username).first()
        if exist: raise ValidationError(f"Já existe um usuário cadastrado para esse nome de usuário.", code='invalid')
        return username







 # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     add_attr(self.fields['username'], 'placeholder', 'Insira o usuário')
    #     add_attr(self.fields['email'], 'placeholder', 'Insira o email')
    #     add_attr(self.fields['password'], 'placeholder', 'Insira sua senha desejada')
    
        

    # class Meta:
    #     model = User
    #     fields = [
    #         "username", "email", "password"
    #     ]        


    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     email_exist = User.objects.get(email=email)
    #     if email_exist:
    #         raise ValidationError('Esse e-mail já está sendo usado', code='invalid')
