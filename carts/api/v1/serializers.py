from rest_framework import serializers
from carts.models import Cart, CartItem
from productpacks.models import ProductPack
from discount.models import DiscountCode
from django.shortcuts import get_object_or_404
from users.api.v1.serializers import UserSerializer
from productpacks.api.v1.serializers import ListProductPacksSerializer


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = []

    def create(self, user, validated_data):
        return Cart.objects.create(user=user, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Cart
        fields = [
            "created_time",
            "updated_time",
            "user"
        ]


class CartItemSerializer(serializers.ModelSerializer):
    item = ListProductPacksSerializer(many=False)
    class Meta:
        model = CartItem
        fields = ['item', 
                  'quantity',
                  "price"
                ]


class CartItemCreateSerializer(serializers.ModelSerializer):
    discount_code = serializers.CharField(max_length=30)
    price = serializers.HiddenField(default = 0)
    class Meta:
        model = CartItem
        fields = [
            'quantity', 
            "discount_code",
            "price"
        ]

    def validate_discount_code(self, value):
        product_pack_sku = self.context.get("product_pack_sku")
        product_pack = ProductPack.objects.get(sku = product_pack_sku)
        if not value:
            self.price = product_pack.price
            return value
        discount_code = DiscountCode.objects.filter(code = value).first()
        if not discount_code:
            raise serializers.ValidationError("discount code doesn't exists!")
        code_product_discounts = set(discount_code.product_discounts.filter(black_list=None))
        
        pack_product_discounts = set(product_pack.product_discounts.filter(black_list=None))
        intersection_discounts = list(code_product_discounts & pack_product_discounts)
        if not intersection_discounts:
            raise serializers.ValidationError("there isn't any available discount code with the code you provided for this product pack!")
        product_discount = intersection_discounts[0]
        self.price = product_discount.new_price
        return value


    def create(self, cart_sku, product_pack_sku, validated_data):
        discount_code = validated_data.pop("discount_code")
        validated_data['price'] = self.price
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
        validated_data["discount_code"] = discount_code
        return item


