from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from usuarios.models import Usuario
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

class UsuarioViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario_data = {
            'username': 'testuser',
            'email_institucional': 'testuser@alunos.ufersa.edu.br',
            'nome_completo': 'Test User',
            'matricula': '20210001',
            'curso': 'Ciência da Computação',
            'password': 'testpassword',
            'confirmacao_senha': 'testpassword'
        }
        self.url = reverse('usuario-list')  # Assumindo que você está usando DefaultRouter

    def test_create_usuario(self):
        response = self.client.post(self.url, self.usuario_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(Usuario.objects.get().email_institucional, 'testuser@alunos.ufersa.edu.br')

    def test_create_usuario_invalid_data(self):
        invalid_data = self.usuario_data.copy()
        invalid_data['email_institucional'] = 'invalid_email'
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class AtivarContaTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            username='testuser',
            email_institucional='testuser@alunos.ufersa.edu.br',
            password='testpassword'
        )
        self.user.is_active = False
        self.user.save()
        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)

    def test_ativar_conta(self):
        url = reverse('activate', kwargs={'uidb64': self.uid, 'token': self.token})
        response = self.client.get(url)
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)
        self.assertRedirects(response, reverse('login'))

    def test_ativar_conta_invalid_token(self):
        url = reverse('activate', kwargs={'uidb64': self.uid, 'token': 'invalid-token'})
        response = self.client.get(url)
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
        self.assertEqual(response.status_code, 200)  # Assumindo que você está renderizando uma página de erro

