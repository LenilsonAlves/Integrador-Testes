from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=255)  # Nome da empresa
    cnpj = models.CharField(max_length=18, unique=True)  # CNPJ (Cadastro Nacional de Pessoa Jurídica)
    endereco = models.CharField(max_length=255)  # Endereço
    telefone = models.CharField(max_length=20)  # Telefone
    email = models.EmailField(unique=True)  # E-mail
    setor_atuacao = models.CharField(max_length=100)  # Setor de atuação
    site = models.URLField(null=True, blank=True)  # Site (opcional)
    descricao = models.TextField()  # Descrição
    foto_perfil = models.ImageField(upload_to='fotos_empresa/', null=True, blank=True)  # Foto do perfil (opcional)
    redes_sociais = models.JSONField(null=True, blank=True)  # Redes sociais (opcional)

    def __str__(self):
        return self.nome
