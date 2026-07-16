from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet

router = DefaultRouter()
router.register('products', ProductModelViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]