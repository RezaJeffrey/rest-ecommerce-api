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
            'likes', 'replies'
        ]

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        fields['reply_comment'] = CommentSerializer(many=False)
        return fields


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'reply_comment',
            'text'
        ]

    def create(self, user, **validated_data):
        return Comment.objects.create(
            user=user,
            **validated_data
        )





