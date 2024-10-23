from rest_framework import viewsets
from .models import Oportunidade
from .serializers import OportunidadeSerializer

class OportunidadeViewSet(viewsets.ModelViewSet):
    queryset = Oportunidade.objects.all()
    serializer_class = OportunidadeSerializer
