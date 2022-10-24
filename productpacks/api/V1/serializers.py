from rest_framework import serializers
from productpacks.models import ProductPack
from products.models import ExtraFieldValue, Product


class ProductPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPack
        fields = [
            'product', 'extra_field_values',
        ]

    def get_fields(self):
        product = Product.objects.get(
            sku=self.context['product_sku']
        )
        self.fields['extra_field_values'] = serializers.PrimaryKeyRelatedField(
            queryset=ExtraFieldValue.objects.filter(
                product=product
            ),
        )

    def create(self, **validated_data):
        values = validated_data.pop('extra_field_values')
        product_pack = ProductPack.objects.create(
            **validated_data
        )
        product_pack.extra_field_values.add(*values)
        return product_pack


