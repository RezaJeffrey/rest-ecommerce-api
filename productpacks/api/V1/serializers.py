from rest_framework import serializers
from productpacks.models import ProductPack
from products.models import ExtraFields


class ProductPackSerializer(serializers.ModelSerializer):
    field = ExtraFields(many=False)

    class Meta:
        model = ProductPack
        fields = [
            'field', 'value'
        ]



