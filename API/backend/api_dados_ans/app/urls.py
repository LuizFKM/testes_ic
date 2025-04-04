from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.viewsets import OperadoraViewSet

router = DefaultRouter()
router.register(r'operadoras', OperadoraViewSet, basename='operadora')

urlpatterns = [
    path('', include(router.urls)),
]