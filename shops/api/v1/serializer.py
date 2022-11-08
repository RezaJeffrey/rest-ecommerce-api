from rest_framework import serializers
from shops.models import Shop, ShopAddress


class ShopAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopAddress
        fields = [
            'address', 'postal_code'
        ]


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'name', 'address',
            'province'
        ]





