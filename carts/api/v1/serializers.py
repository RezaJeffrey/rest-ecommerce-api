from rest_framework import serializers
from carts.models import Cart, CartItem
from productpacks.models import ProductPack
from django.shortcuts import get_object_or_404


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = []

    def create(self, user, validated_data):
        return Cart.objects.create(user=user, **validated_data)


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'quantity'
        ]

    def create(self, cart_sku, product_pack_sku, validated_data):
        cart = get_object_or_404(
            Cart,
            sku=cart_sku
        )
        pack = get_object_or_404(
            ProductPack,
            sku=product_pack_sku
        )
        item = CartItem.objects.create(
            cart=cart,
            item=pack,
            **validated_data
        )
        return item


