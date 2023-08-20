from products.models import Product, ProductImage
from extra_fields.models import ExtraFieldValue, ExtraFieldName
from category.models import Category
from rest_framework import serializers
from likes.api.v1.serializer import LikeSerializer
from comments.api.v1.serializer import CommentSerializer
from extra_fields.api.v1.serializer import ExtraFieldSerializer
from django.shortcuts import get_object_or_404

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            "image", "alt_text"
        ]

class ProductImageCreateSerializer(serializers.ModelSerializer):
    product_sku = serializers.CharField(max_length = 255)
    class Meta:
        model = ProductImage
        fields = [
            "product_sku", "image",
            "alt_text" 
        ]
    def create(self, validated_data):
        product = get_object_or_404(Product, sku=validated_data.get("product_sku"))
        return ProductImage.objects.create(product=product, image=validated_data.get("image"), alt_text=validated_data.get("alt_text"))

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(child=None)
    )
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'description', 'brand',
            'shop', 'images',
            'likes', 'comments'
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'category',
            'description', 'brand',
            'shop'
        ]

    def create(self, validated_data):
        shop = validated_data.pop('shop')
        product = Product.objects.create(**validated_data)
        for shop in shop:
            product.shop.add(shop)
        return product
