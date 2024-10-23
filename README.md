# Back Projeto João

Este projeto é uma aplicação Django com Django Rest Framework, servindo como base para uma API. Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

### Passo a passo para iniciar o projeto

## 1. Clonar o repositório

Primeiro, clone este repositório para sua máquina local:
git clone git@github.com:six-org/sistema-para-divulgacao-de-estagio-projetos_back-end.git

## 2. Acessar o diretório do projeto
cd back-projeto-joao

## 3. Criar e ativar o ambiente virtual
Crie um ambiente virtual:
python -m venv venv
---------------------------------------------------
Ative o ambiente virtual:

    -No Windows:
            venv\Scripts\activate
    -No Linux/macOS:
            source venv/bin/activate

## 4. Instalar as dependências
Instale as dependências:
pip install -r requirements.txt

## 5. Criar o banco de dados
Crie o banco de dados:
python manage.py migrate

## 6. Criar o usuário administrador
Crie o usuário administrador:
python manage.py createsuperuser

## 7. Iniciar o servidor
Inicie o servidor:
python manage.py runserver

## 8. Acessar o site
Acesse o site em http://localhost:8000/




### Passo a passo para criar uma API
    Passo a passo para criar uma API simples usando Django Rest Framework:

## 1. Criar um novo app
Crie um novo app:
python manage.py startapp nome-do-app

## Registrando o app
    Depois disso, registre o app no arquivo settings.py:

    INSTALLED_APPS = [
        ...
        'nome-do-app',
        ...
    ]

## 2. Criar uma nova API
Crie uma nova API:
Criar um modelo:
    Exemplo:
        from django.db import models

        class Produto(models.Model):
            nome = models.CharField(max_length=100)
            preco = models.DecimalField(max_digits=10, decimal_places=2)
            quantidade = models.IntegerField()
Criar o Serializer:
    Exemplo:
        from rest_framework import serializers
        from .models import Produto

        class ProdutoSerializer(serializers.ModelSerializer):
            class Meta:
                model = Produto
                fields = ['nome', 'preco', 'quantidade']
Criar a View:
    Exemplo:
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from .models import Produto
    from .serializers import ProdutoSerializer

    class ProdutoView(APIView):
        def get(self, request):
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
            return Response(serializer.data)

        def post(self, request):
            serializer = ProdutoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
Criar a URL:
    Exemplo:
        from django.urls import path
        from .views import ProdutoView

        urlpatterns = [
            path('produtos/', ProdutoView.as_view()),
        ]
    Em seguida, registrar a URL no arquivo urls.py:

        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/', include('nome-do-app.urls')),
        ]

## 3. Testar a API
Testar a API:
Abra o navegador e acesse a URL http://localhost:8000/produtos/


