from category.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']

    def create(self, **validated_data):
        return Category.objects.create(**validated_data)
