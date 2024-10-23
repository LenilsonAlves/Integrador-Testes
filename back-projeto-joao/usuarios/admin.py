from django.contrib import admin
from .models import Usuario  # Importe o modelo que você quer registrar

# Registrar o modelo no Django Admin
admin.site.register(Usuario)
