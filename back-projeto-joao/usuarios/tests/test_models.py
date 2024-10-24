from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from usuarios.models import Usuario
from django.conf import settings
from django.core import mail
from django.test.client import RequestFactory
from unittest.mock import patch

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            username="testuser",
            email_institucional="testuser@alunos.ufersa.edu.br",
            nome_completo="Test User",
            matricula="20210001",
            curso="Ciência da Computação"
        )

    def test_create_usuario(self):
        self.assertTrue(isinstance(self.usuario, Usuario))
        self.assertEqual(self.usuario.__str__(), self.usuario.nome_completo)

    def test_email_institucional_validator(self):
        usuario_invalido = Usuario(
            username="invaliduser",
            email_institucional="invalid@gmail.com",
            nome_completo="Invalid User",
            matricula="20210002",
            curso="Engenharia"
        )
        with self.assertRaises(ValidationError):
            usuario_invalido.full_clean()

    def test_campos_opcionais(self):
        self.assertIsNone(self.usuario.email_pessoal)
        self.assertIsNone(self.usuario.telefone_contato)
        self.assertFalse(bool(self.usuario.foto_perfil))
        self.assertIsNone(self.usuario.redes_sociais)

    def test_foto_perfil_upload(self):
        file_content = b"file_content"
        file = SimpleUploadedFile("test_image.jpg", file_content, content_type="image/jpeg")
        self.usuario.foto_perfil = file
        self.usuario.save()
        self.assertTrue(self.usuario.foto_perfil.name.startswith('fotos_perfil/'))

    def test_redes_sociais_json(self):
        redes_sociais = {
            "instagram": "https://instagram.com/testuser",
            "linkedin": "https://linkedin.com/in/testuser"
        }
        self.usuario.redes_sociais = redes_sociais
        self.usuario.save()
        self.assertEqual(self.usuario.redes_sociais, redes_sociais)

    def test_enviar_email_validacao(self):
        request = RequestFactory().get('/')
        with patch('django.core.mail.send_mail') as mock_send_mail:
            self.usuario.enviar_email_validacao(request)
            self.assertTrue(mock_send_mail.called)
            call_args = mock_send_mail.call_args
            self.assertEqual(call_args[1]['subject'], "Ativação de conta")
            self.assertEqual(call_args[1]['recipient_list'], [self.usuario.email_institucional])

    def test_groups_e_permissions(self):
        self.assertEqual(self.usuario.groups.count(), 0)
        self.assertEqual(self.usuario.user_permissions.count(), 0)
