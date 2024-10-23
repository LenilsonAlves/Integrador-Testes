from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatMensagemViewSet, FAQViewSet

router = DefaultRouter()
router.register(r'chat', ChatMensagemViewSet)
router.register(r'faq', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
