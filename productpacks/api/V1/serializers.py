from rest_framework import serializers
from products.models import Product
from extra_fields.models import ExtraFieldValue
from productpacks.models import ProductPack


class ProductPackCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Product.objects.all()
    )
    extra_field_values = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ExtraFieldValue.objects.all()
    )

    class Meta:
        model = ProductPack
        fields = [
            'product',
            'extra_field_values',
            'stock', 'price'
        ]

    def create(self, validated_data):
        product_pack = ProductPack.objects.create(
            product=validated_data['product'],
            price=validated_data['price'],
            stock=validated_data['stock'],
        )
        product_pack.extra_field_values.set(validated_data['extra_field_values'])
        return product_pack


class ValueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldValue
        fields = [
            'field_name', 'value'
        ]


class UpdateValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPack
        fields = []

    def validate(self, attrs):
        product_pack_sku = self.context['product_pack_sku']
        value_sku = self.context['value_sku']
        product_pack = ProductPack.objects.get(
            sku=product_pack_sku
        )
        value = ExtraFieldValue.objects.get(
            sku=value_sku
        )
        value_field_name = value.field_name
        queryset = product_pack.extra_field_values.filter(
            field_name=value_field_name
        )
        if not queryset.exists():
            message = 'There isn\'t any value with the field name your value has!'
            raise serializers.ValidationError(message)
        return attrs

    def update(self):
        product_pack = ProductPack.objects.get(
            sku=self.context['product_pack_sku']
        )
        new_value = ExtraFieldValue.objects.get(
            sku=self.context['value_sku']
        )
        pre_value = product_pack.extra_field_values.get(
            field_name=new_value.field_name
        )
        product_pack.extra_field_values.remove(pre_value)
        product_pack.extra_field_values.add(new_value)
        return product_pack


