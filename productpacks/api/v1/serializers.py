from rest_framework import serializers
from products.models import Product
from shops.models import Shop
from extra_fields.models import ExtraFieldValue
from productpacks.models import ProductPack
from products.api.v1.serializer import ProductSerializer
from extra_fields.api.v1.serializer import ExtraFieldSerializer

class GetShopsPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(GetShopsPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None

class ProductPackCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Product.objects.all()
    )
    extra_field_values = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ExtraFieldValue.objects.all()
    )
    shop = GetShopsPrimaryKeyRelatedField(
        many=True,
        queryset=Shop.objects.all()
    )

    class Meta:
        model = ProductPack
        fields = [
            'product',
            'extra_field_values',
            'stock', 'price',
            'shop'
        ]


    def create(self, validated_data):
        product_pack = ProductPack.objects.create(
            product=validated_data['product'],
            price=validated_data['price'],
            stock=validated_data['stock'],
        )
        product_pack.extra_field_values.set(validated_data['extra_field_values'])
        return product_pack

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.extra_field_values = validated_data.get('extra_field_values', instance.extra_field_values)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


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
