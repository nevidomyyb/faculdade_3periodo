from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def send(instance, filename):
    return f"images/{filename}"
class Projeto(models.Model):
    idprojeto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to=send)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    