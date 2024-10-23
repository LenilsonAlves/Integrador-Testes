from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/colaboradores/', include('colaboradores.urls')),
    path('api/comunicacao/', include('comunicacao.urls')),
    path('api/empresas/', include('empresas.urls')),
    path('api/oportunidades/', include('oportunidades.urls')),
    path('api/usuarios/', include('usuarios.urls')), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
