from django.test import TestCase
from usuarios.serializers import UsuarioSerializer
from usuarios.models import Usuario
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

class UsuarioSerializerTest(TestCase):
    def setUp(self):
        self.usuario_data = {
            'username': 'testuser',
            'email_institucional': 'testuser@alunos.ufersa.edu.br',
            'nome_completo': 'Test User',
            'matricula': '20210001',
            'curso': 'Ciência da Computação',
            'password': 'testpassword',
            'confirmacao_senha': 'testpassword'
        }
        self.serializer = UsuarioSerializer(data=self.usuario_data)

    def test_contains_expected_fields(self):
        data = self.serializer.initial_data
        self.assertCountEqual(data.keys(), ['username', 'email_institucional', 'nome_completo', 'matricula', 'curso', 'password', 'confirmacao_senha'])

    def test_password_validation(self):
        self.usuario_data['confirmacao_senha'] = 'wrongpassword'
        serializer = UsuarioSerializer(data=self.usuario_data)
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

    def test_create_user(self):
        serializer = UsuarioSerializer(data=self.usuario_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, Usuario)
        self.assertEqual(user.email_institucional, 'testuser@alunos.ufersa.edu.br')
        self.assertFalse(user.is_active)  # Verifica se a conta está inativa por padrão
