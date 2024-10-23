from rest_framework import serializers
from .models import Colaborador

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = [
            'id', 'nome', 'tipo_usuario', 'departamento', 'cargo', 'email_institucional', 
            'email_pessoal', 'telefone', 'foto_perfil', 'redes_sociais'
        ]
