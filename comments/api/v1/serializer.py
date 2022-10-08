from rest_framework import serializers
from comments.models import Comment
from likes.api.v1.serializer import LikeSerializer


class CommentSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True)

    class Meta:
        model = Comment
        fields = [
            'user', 'text',
            'created_time',
            'reply_comment',
            'likes'
        ]

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        fields['reply_comment'] = CommentSerializer(many=True)
        return fields


class CreateCommentSerializer(serializers.ModelSerializer):
    pass






