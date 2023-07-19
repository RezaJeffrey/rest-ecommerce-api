from rest_framework import serializers
from orders.models import Order, OrderStatus
from carts.api.v1.serializers import CartSerializer
from address.api.v1.serializers import AddressSerializer


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = [
            'status'
        ]

    def update(self, instance, **validated_data):
        instance.status = validated_data.get('status', instance.status)
        return instance.save()


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer(many=False)
    order_cart = CartSerializer(many=False)
    address = AddressSerializer(many=False)

    class Meta:
        model = Order
        fields = [
            'status', 'address',
            'order_cart', 'payment_method'
        ]


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'address', 'payment_method',
        ]
    # TODO [BUG]bug here (anony user has no attr address)

    # def get_fields(self):
    #     user = self.context['user']
    #     fields = super(OrderCreateUpdateSerializer, self).get_fields()
    #     fields['address'] = serializers.PrimaryKeyRelatedField(
    #         queryset=user.addresses.all()
    #     )
    #     return fields

    def create(self, user, **validated_data):
        order_cart = user.cart
        order = Order.objects.create(
            user=user,
            order_cart=order_cart,
            **validated_data
        )
        return OrderStatus.objects.create(
            order=order
        )
