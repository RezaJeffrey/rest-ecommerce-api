from products.models import Product, ExtraFieldName, ExtraFieldValue
from category.models import Category
from rest_framework import serializers
from likes.api.v1.serializer import LikeSerializer
from comments.api.v1.serializer import CommentSerializer


class ExtraFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldName
        fields = ['name']


class ExtraFieldSerializer(serializers.ModelSerializer):
    field_name = serializers.PrimaryKeyRelatedField(
        queryset=ExtraFieldName.objects.all()
    )
    product = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True,
    )

    class Meta:
        model = ExtraFieldValue
        fields = ['field_name', 'value', 'product']

    def create(self, product_sku, **validated_data):
        product = Product.objects.get(
            sku=product_sku
        )
        field_value = ExtraFieldValue.objects.create(
            product=product,
            **validated_data
        )
        return field_value


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(child=None)
    )
    extra_fields = ExtraFieldSerializer(many=True)
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'description', 'brand',
            'shop', 'extra_fields',
            'likes', 'comments'
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'description', 'brand',
            'shop',
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
