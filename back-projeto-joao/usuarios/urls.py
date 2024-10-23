from django.urls import path
from .views import ativar_conta, UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UsuarioViewSet)  # Registrando as rotas de CRUD para os usuários

urlpatterns = [
    path('activate/<uidb64>/<token>/', ativar_conta, name='activate'),  # Rota para ativar conta
]

urlpatterns += router.urls
