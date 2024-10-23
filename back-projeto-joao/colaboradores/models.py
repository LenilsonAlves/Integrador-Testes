from django.db import models

class Colaborador(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('Professor', 'Professor'),
        ('Administrativo', 'Administrativo'),
        ('Grupo de Pesquisa', 'Grupo de Pesquisa'),
    ]

    nome = models.CharField(max_length=255)  # Nome do colaborador
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES)  # Tipo de usuário
    departamento = models.CharField(max_length=100)  # Departamento
    cargo = models.CharField(max_length=100)  # Cargo
    email_institucional = models.EmailField(unique=True)  # E-mail institucional
    email_pessoal = models.EmailField(null=True, blank=True)  # E-mail pessoal (opcional)
    telefone = models.CharField(max_length=20, null=True, blank=True)  # Telefone (opcional)
    foto_perfil = models.ImageField(upload_to='fotos_colaboradores/', null=True, blank=True)  # Foto do perfil (opcional)
    redes_sociais = models.JSONField(null=True, blank=True)  # Redes sociais (opcional)

    def __str__(self):
        return self.nome
