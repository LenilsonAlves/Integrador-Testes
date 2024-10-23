from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator as token_generator

class Usuario(AbstractUser):
    email_institucional = models.EmailField(unique=True, validators=[RegexValidator(
    regex=r'^.+@alunos\.ufersa\.edu\.br$', message='O e-mail deve ser um e-mail institucional (@alunos.ufersa.edu.br).')])
    email_pessoal = models.EmailField(null=True, blank=True)
    nome_completo = models.CharField(max_length=255)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    telefone_contato = models.CharField(max_length=20, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    redes_sociais = models.JSONField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )

    def __str__(self):
        return self.nome_completo

    # Método para enviar o e-mail de ativação
    def enviar_email_validacao(self, request):
        # Gera o token de ativação
        token = token_generator.make_token(self)
        uid = urlsafe_base64_encode(force_bytes(self.pk))

        # Gera a URL de ativação
        activation_url = f"{request.scheme}://{request.get_host()}/api/usuarios/activate/{uid}/{token}/"

        # Renderiza o conteúdo do e-mail usando um template
        message = render_to_string('activation_email.html', {
            'user': self,
            'activation_url': activation_url,
        })

        # Envia o e-mail
        send_mail(
            subject="Ativação de conta",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email],
        )
