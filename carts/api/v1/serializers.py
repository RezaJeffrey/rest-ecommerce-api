from rest_framework import serializers
from carts.models import Cart, CartItem
from productpacks.models import ProductPack
from django.shortcuts import get_object_or_404
from productpacks.api.v1.serializers import ListProductPacksSerializer


class CartItemSerializer(serializers.ModelSerializer):
    # item = ListProductPacksSerializer()

    class Meta:
        model = CartItem
        fields = ['__str__', 'quantity', 'total_price', 'discount_code']


class CartItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['item', 'quantity', 'total_price', 'discount_code']

    def create(self, cart_sku, product_pack_sku, validated_data):
        cart = get_object_or_404(Cart, sku=cart_sku)
        pack = get_object_or_404(ProductPack, sku=product_pack_sku)
        if pack.stock > validated_data.get('quantity'):
            item = CartItem.objects.create(
                cart=cart,
                **validated_data
            )
            new_stock = pack.stock - validated_data.get('quantity')
            pack.update_stock(new_stock=new_stock)
        else:
            raise ValueError('not enough stock')
        return item


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)
    cart_totol_price = serializers.DecimalField(max_digits=10, decimal_places=2)

