from rest_framework import serializers
from productpacks.models import ProductPack
from products.api.v1.serializers import ProductSerializer, ExtraFieldSerializer


class ProductPackSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    extra_field_value = ExtraFieldSerializer(many=False)

    class Meta:
        model = ProductPack
        fields = [
            'product', 'extra_field_value'
        ]



