from rest_framework import serializers
from .models import Usuario
from django.core.exceptions import ValidationError

class UsuarioSerializer(serializers.ModelSerializer):
    confirmacao_senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nome_completo', 'email_institucional', 'matricula', 'curso', 'password', 'confirmacao_senha',
                  'email_pessoal', 'telefone_contato', 'foto_perfil', 'redes_sociais']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        # Validação de confirmação de senha
        if data['password'] != data['confirmacao_senha']:
            raise ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmacao_senha')
        password = validated_data.pop('password')

        # Criar o usuário e configurar a senha corretamente
        usuario = Usuario(**validated_data)
        usuario.set_password(password)  # Hash a senha usando o método set_password
        usuario.is_active = False  # Desativa a conta até a ativação por e-mail
        usuario.save()

        return usuario
