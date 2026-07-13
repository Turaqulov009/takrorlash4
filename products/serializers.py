from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","price","description"]
        read_only_fields=["id"]