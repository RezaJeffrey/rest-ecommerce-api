from discount.models import DiscountCode, ProductDiscount
from rest_framework import serializers


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = [
            "code", "available_untill"
        ]

    def create(self, validated_data):
        discount_code = DiscountCode.objects.create(**validated_data)
        return discount_code

    def update(self, instance, validated_data):
        instance.code = validated_data.get("code", instance.code)
        instance.available_untill = validated_data.get("available_untill", instance.available_untill)
        instance.save()
        return instance


class ProductDiscountSerializer(serializers.ModelSerializer):
    discount_code = DiscountCodeSerializer()
    class Meta:
        model = ProductDiscount
        fields = [
            "discount_code", "percent"
        ]

    def create(self, validated_data, product_pack):
        new_price = product_pack.price * validated_data["percent"] / 100
        discount_code = DiscountCode.objects.create(**validated_data["discount_code"])
        product_discount = ProductDiscount.objects.create(
            product_pack = product_pack,
            discount_code = discount_code,
            new_price = new_price,
            percent = validated_data["percent"]
        )
        return product_discount

    def update(self, instance, validated_data):
        instance.percent = validated_data.get("percent", instance.percent)
        instance.save()
        return instance
