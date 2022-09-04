from category.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', 'child']


class CategorySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']

    def create(self, **validated_data):
        return Category.objects.create(**validated_data)
