from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers