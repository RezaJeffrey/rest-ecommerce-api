from rest_framework import serializers
from productpacks.models import ProductPack
from products.models import ExtraFieldValue, Product


class ProductPackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPack
        fields = []

    def create(self, product_sku):
        product = Product.objects.get(
            sku=product_sku
        )
        return ProductPack.objects.create(
            product=product
        )


class AddValueToPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPack
        fields = []

    def validate(self, attrs):
        product_pack_sku = self.context.get('view').kwargs['product_pack_sku']
        value_sku = self.context.get('view').kwargs['value_sku']
        product_pack = ProductPack.objects.get(
            sku=product_pack_sku
        )
        value = ExtraFieldValue.objects.get(
            sku=value_sku
        )
        product_for_pack = product_pack.product
        product_for_value = value.product
        if product_for_pack != product_for_value:
            message = 'the value you want to add is referencing to an other product!'
            raise serializers.ValidationError(message)
        return attrs

    def create(self, product_pack_sku, value_sku):
        product_pack = ProductPack.objects.get(
            sku=product_pack_sku
        )
        value = ExtraFieldValue.objects.get(
            sku=value_sku
        )
        return product_pack.extra_field_values.add(value)


class ValueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldValue
        fields = [
            'field_name', 'value'
        ]

