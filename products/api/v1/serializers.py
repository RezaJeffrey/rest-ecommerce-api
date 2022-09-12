from products.models import Product, ProductPack
from rest_framework import serializers
from eav.models import Attribute
from category.api.v1.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'brand', 'shop',
            'description'
        ]

    def create(self, validated_data):
        Product.objects.create(**validated_data)

