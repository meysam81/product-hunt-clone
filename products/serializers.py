from .models import Product
from rest_framework import serializers as sz


class ProductSerializer(sz.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
