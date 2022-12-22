from rest_framework.serializers import ModelSerializer
from shops.models import Shop
from discount.models import DiscountCode


class DiscountCodeSerializer(ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = ['code', 'percent', 'discount_limit', 'available_until', 'amount', 'is_active', 'sku']
        extra_kwargs = {
            'amount': {'style': {'placeholder': "leave blank if no need"}}
        }

    def create(self, user, **validated_data):
        shop = Shop.objects.get(shopstaf__user=user)
        return DiscountCode.objects.create(
            shop=shop,
            **validated_data
        )
