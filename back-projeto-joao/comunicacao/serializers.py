from rest_framework import serializers
from .models import ChatMensagem

class ChatMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMensagem
        fields = ['id', 'aluno', 'empresa', 'mensagem', 'data_hora', 'lida']


from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'pergunta', 'resposta', 'data_criacao']
