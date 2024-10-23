from rest_framework import viewsets
from .models import ChatMensagem
from .serializers import ChatMensagemSerializer

class ChatMensagemViewSet(viewsets.ModelViewSet):
    queryset = ChatMensagem.objects.all()
    serializer_class = ChatMensagemSerializer


from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
