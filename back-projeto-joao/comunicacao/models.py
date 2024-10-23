from django.db import models
from django.conf import settings
from empresas.models import Empresa

class ChatMensagem(models.Model):
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Aluno (usuário)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Empresa
    mensagem = models.TextField()  # Conteúdo da mensagem
    data_hora = models.DateTimeField(auto_now_add=True)  # Data e Hora da mensagem
    lida = models.BooleanField(default=False)  # Mensagem lida

    def __str__(self):
        return f'{self.aluno} -> {self.empresa}: {self.mensagem[:20]}'


class FAQ(models.Model):
    pergunta = models.CharField(max_length=255)  # Pergunta
    resposta = models.TextField()  # Resposta
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.pergunta
