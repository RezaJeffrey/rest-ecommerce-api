from rest_framework import serializers
from extra_fields.models import ExtraFieldValue, ExtraFieldName
from products.models import Product


class ExtraFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldName
        fields = ['name']


class ExtraFieldSerializer(serializers.ModelSerializer):
    field_name = serializers.PrimaryKeyRelatedField(
        queryset=ExtraFieldName.objects.all()
    )
    product = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True,
    )

    class Meta:
        model = ExtraFieldValue
        fields = ['field_name', 'value', 'product']

    def create(self, product_sku, **validated_data):
        product = Product.objects.get(
            sku=product_sku
        )
        field_value = ExtraFieldValue.objects.create(
            product=product,
            **validated_data
        )
        return field_value
