from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id', 'nome', 'cnpj', 'endereco', 'telefone', 'email', 'setor_atuacao',
            'site', 'descricao', 'foto_perfil', 'redes_sociais'
        ]
