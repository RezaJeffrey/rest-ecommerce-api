from products.models import Product, ExtraFieldName, ExtraFieldValue, Brand, Shop, ShopAddress
from category.models import Category
from rest_framework import serializers
from likes.api.v1.serializer import LikeSerializer
from comments.api.v1.serializer import CommentSerializer


class ExtraFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldName
        fields = ['name']


class ExtraFieldValueSerializer(serializers.ModelSerializer):
    field_name = serializers.PrimaryKeyRelatedField(
        queryset=ExtraFieldName.objects.all()
    )
    value = serializers.CharField(
        many=False,
        read_only=True,
    )

    class Meta:
        model = ExtraFieldValue
        fields = ['field_name', 'value']
        # TODO fix this create function

    # def create(self, product_sku, **validated_data):
    #     product = Product.objects.get(
    #         sku=product_sku
    #     )
    #     field_value = ExtraFieldValue.objects.create(
    #         product=product,
    #         **validated_data
    #     )
    #     return field_value
    #


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name', 'image'
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopAddress
        fields = [
            'address', 'postal_code'
        ]


class ShopSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)

    class Meta:
        model = Shop
        fields = [
            'name', 'province', 'address',
        ]


class AttrValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldValue
        fields = [
            'value', "field_name"
        ]


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.filter(child=None)
    # )
    extra_fields = ExtraFieldValueSerializer(many=True)

    brand = BrandSerializer(many=True)
    shop = ShopSerializer(many=True)
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)
    attribute_values = AttrValuesSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name', 'description',
            'category',
            'brand',
            'shop', 'likes',
            'comments', 'sku',
            'attribute_values',
            'store_price', 'sale_price',
            'is_active', 'is_default',
            'in_stock'
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)




