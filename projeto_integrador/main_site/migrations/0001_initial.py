# Generated by Django 4.2.4 on 2023-09-02 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main_site.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('idprojeto', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to=main_site.models.send)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
