from rest_framework import serializers
from address.models import Address
from rest_framework.validators import ValidationError


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'mode', 'name',
            'address', 'post_code'
        ]

    def validate_post_code(self, postal_code):
        if len(postal_code) != 10:
            raise ValidationError('postal code must be only 10 digits')
        for i in ['0', '2', '5']:
            if i in postal_code[0:5]:
                raise ValidationError('format is not accepted')

        return postal_code

    def create(self, user, validated_data):
        return Address.objects.create(
            user=user,
            **validated_data
        )
