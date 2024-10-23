from rest_framework import serializers
from .models import Oportunidade

class OportunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oportunidade
        fields = [
            'id', 'titulo', 'tipo', 'descricao', 'requisitos', 'localizacao',
            'carga_horaria', 'remuneracao', 'data_inicio', 'data_termino',
            'empresa', 'numero_vagas', 'anexos', 'forma_selecao',
            'categoria_tags', 'cursos_desejados'
        ]
