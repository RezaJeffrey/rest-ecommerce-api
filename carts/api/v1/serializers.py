from rest_framework import serializers
from carts.models import Pack, Cart
from products.api.v1.serializers import ExtraFieldValue


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = [
            'product',
            'extra_field_names',
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'paks'
        ]






