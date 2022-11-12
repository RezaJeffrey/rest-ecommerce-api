from django.urls import path
from .view import AddLikeComment

app_name = 'comment'

urlpatterns = [
    path('comment/<int:comment_pk>/<str:comment_sku>/add_like', AddLikeComment.as_view(), name='add_like')
]
