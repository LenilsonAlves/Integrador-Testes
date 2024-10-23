# Generated by Django 5.1.1 on 2024-09-24 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('setor_atuacao', models.CharField(max_length=100)),
                ('site', models.URLField(blank=True, null=True)),
                ('descricao', models.TextField()),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotos_empresa/')),
                ('redes_sociais', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
