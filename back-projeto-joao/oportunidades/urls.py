from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OportunidadeViewSet

router = DefaultRouter()
router.register(r'', OportunidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
