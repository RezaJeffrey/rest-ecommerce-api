from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'mode', 'name',
            'address', 'post_code'
        ]

    def create(self, user, validated_data):
        return Address.objects.create(
            user=user,
            **validated_data
        )



