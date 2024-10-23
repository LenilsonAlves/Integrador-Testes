from django.db import models
from empresas.models import Empresa 

class Oportunidade(models.Model):
    TIPO_CHOICES = [
        ('Estágio', 'Estágio'),
        ('Projeto de Pesquisa', 'Projeto de Pesquisa'),
        ('Projeto de Extensão', 'Projeto de Extensão'),
        ('Emprego', 'Emprego'),
    ]
    
    titulo = models.CharField(max_length=255)  # Título da oportunidade
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)  # Tipo de oportunidade
    descricao = models.TextField()  # Descrição da oportunidade
    requisitos = models.TextField()  # Requisitos
    localizacao = models.CharField(max_length=255)  # Localização
    carga_horaria = models.IntegerField()  # Carga horária
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2)  # Remuneração
    data_inicio = models.DateField()  # Data de início
    data_termino = models.DateField()  # Data de término
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='oportunidades')  # Relacionamento com Empresa
    numero_vagas = models.IntegerField()  # Número de vagas
    anexos = models.FileField(upload_to='anexos/', null=True, blank=True)  # Anexos (opcional)
    forma_selecao = models.CharField(max_length=255)  # Forma de seleção
    categoria_tags = models.CharField(max_length=255)  # Categoria/Tags
    cursos_desejados = models.CharField(max_length=255)  # Cursos Desejados

    def __str__(self):
        return self.titulo
