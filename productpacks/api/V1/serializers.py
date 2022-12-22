from rest_framework import serializers
from products.models import Product
from extra_fields.models import ExtraFieldValue
from productpacks.models import ProductPack
from products.api.v1.serializer import ProductSerializer
from extra_fields.api.v1.serializer import ExtraFieldSerializer


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


class ListProductPacksSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    extra_field_values = ExtraFieldSerializer(many=True)

    class Meta:
        model = ProductPack
        fields = [
            'id', 'sku',
            'product',
            'extra_field_values',
            'stock', 'price'
        ]


class UpdateValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPack
        fields = []

    # TODO BUG
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
