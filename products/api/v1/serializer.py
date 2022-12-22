from products.models import Product
from extra_fields.models import ExtraFieldValue, ExtraFieldName
from category.models import Category
from rest_framework import serializers
from likes.api.v1.serializer import LikeSerializer
from comments.api.v1.serializer import CommentSerializer
from extra_fields.api.v1.serializer import ExtraFieldSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(child=None)
    )
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'description', 'brand',
            'shop',
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
        shop = validated_data.pop('shop')
        product = Product.objects.create(**validated_data)
        for shop in shop:
            product.shop.add(shop)
        return product
