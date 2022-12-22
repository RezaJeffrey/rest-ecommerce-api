from rest_framework import serializers
from extra_fields.models import ExtraFieldValue, ExtraFieldName
from products.models import Product


class ExtraFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFieldName
        fields = ['name']

    def create(self, validated_data):
        name = validated_data.pop('name')
        return ExtraFieldName.objects.create(
            name=name,
            **validated_data
        )


class ExtraFieldSerializer(serializers.ModelSerializer):
    field_name = ExtraFieldNameSerializer()

    class Meta:
        model = ExtraFieldValue
        fields = ['field_name', 'value']

    def create(self, **validated_data):

        field_value = ExtraFieldValue.objects.create(
            **validated_data
        )
        return field_value


