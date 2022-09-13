from abc import ABC

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


class AddFieldSerializer(serializers.Serializer):
    choices = [
        ('TYPE_INT', 'integer'),
        ('TYPE_FLOAT', 'float'),
        ('TYPE_TEXT', 'text'),
        ('TYPE_DATE', 'date'),
        ('TYPE_BOOLEAN', 'boolean'),
        ('TYPE_OBJECT', 'object'),
        ('TYPE_ENUM', 'enum'),
        ('TYPE_JSON', 'json'),
        ('TYPE_CSV', 'csv')
    ]
    optional_field_name = serializers.CharField(
        max_length=255,
        allow_blank=False
    )
    optional_field_datatype = serializers.ChoiceField(
        choices=choices,
        allow_blank=False
    )

    def create_attribute(self, optional_name, optional_datatype):
        return Attribute.objects.create(
            name=optional_name,
            datatype=optional_datatype
        )


class ProductPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPack
        fields = [
            'product'
        ]

    def create(self, validated_data):
        return ProductPack.objects.create(**validated_data)


