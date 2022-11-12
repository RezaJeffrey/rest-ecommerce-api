from likes.models import Like
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'created_time']




