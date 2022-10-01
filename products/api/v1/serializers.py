from products.models import Product, ExtraFieldName, ExtraFieldValue
from category.models import Category
from category.api.v1.serializers import CategorySerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(child=None)
    )

    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'description', 'brand',
            'shop'
        ]


class ExtraFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldName
        fields = ['name']


class ExtraFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldValue
        fields = ['field_name', 'value']

    def create(self, product_sku, **validated_data):
        product = Product.objects.get(
            sku=product_sku
        )
        field_value = ExtraFieldValue.objects.create(
            product=product,
            **validated_data
        )
        return field_value
