# Generated by Django 4.2.4 on 2023-09-05 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_alter_projeto_imagem_redimensionada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='imagem_redimensionada',
        ),
    ]
