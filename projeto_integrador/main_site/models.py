from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import os
import shutil
from pi.settings import MEDIA_ROOT
# Create your models here.

def send(instance, filename):
    return f"images/{filename}"

def sendred(instance, filename):
    return f"images/red-{filename}"
class Projeto(models.Model):
    idprojeto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to=send)
    imagem_redimensionada = ImageSpecField(source='imagem', processors=[ResizeToFill(350, 350)], format='JPEG', options={'quality': 60})
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs) :
        try:
            this = Projeto.objects.get(idprojeto=self.idprojeto)
            if this.imagem != self.imagem:
                if isinstance(this.imagem, InMemoryUploadedFile):
                    # Se a imagem atual for um arquivo em memória, fecha o arquivo antes de excluí-lo
                    this.imagem.file.close()
                try:
                    diretorio = MEDIA_ROOT+'/CACHE/images/images/'
                    conteudo = os.listdir(diretorio)
                    diretorios = [item for item in conteudo if os.path.isdir(os.path.join(diretorio, item))]
                    for diretorioz in diretorios:
                        print(diretorioz)
                        print(os.path.basename(this.imagem.name))
                        if (diretorioz==os.path.basename(this.imagem.name) or diretorioz in os.path.basename(this.imagem.name) or os.path.basename(this.imagem.name) in diretorioz):
                            print("Diretorio excluido")
                            shutil.rmtree(diretorio+diretorioz)
                except:
                    pass
                this.imagem.delete(save=False)
        except Projeto.DoesNotExist:
            pass

        try:
            this = Projeto.objects.get(idprojeto=self.idprojeto)
            if this.imagem_redimensionada != self.imagem_redimensionada:
                if isinstance(this.imagem_redimensionada, InMemoryUploadedFile):
                    this.imagem_redimensionada.file.close()
                this.imagem_redimensionada.delete(save=False)
        except:
            pass
            
        return super(Projeto, self).save(*args, **kwargs)