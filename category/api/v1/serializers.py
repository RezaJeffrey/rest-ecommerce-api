from category.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', 'child']

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['child'] = CategorySerializer(many=True)
        return fields


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
