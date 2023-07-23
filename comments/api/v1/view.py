from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from comments.models import Comment
from rest_framework import status
from rest_framework.response import Response


class AddLikeComment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, comment_pk, comment_sku):
        comment = Comment.objects.get(
            pk=comment_pk,
            sku=comment_sku
        )
        comment.likes.create(
            user=request.user
        )
        response = {
            'message': 'liked successfully!'
        }
        code = status.HTTP_201_CREATED
        return Response(
            data=response,
            status=code
        )








