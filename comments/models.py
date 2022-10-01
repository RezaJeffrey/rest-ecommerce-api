from django.db import models
from products.models import DateTimeMixin

'''
class Comment(DateTimeMixin):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=1200)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:35]


class ReplyComment(DateTimeMixin):
    user = models.ForeignKey(User, related_name='comment_replies', on_delete=models.CASCADE)
    text = models.CharField(max_length=1200)
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text[:30]}...    from user  < {self.user.username}>    replied to    {self.comment.text[:35]}..."


class LikeComment(DateTimeMixin):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    to_comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}     -->    {self.to_comment.text[:35]}..."

'''