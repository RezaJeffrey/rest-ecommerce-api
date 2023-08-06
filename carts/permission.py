from rest_framework.permissions import BasePermission
from carts.models import CartItem
from django.shortcuts import get_object_or_404

class IsCartBelongsToUser(BasePermission):
    def has_permission(self, request, view):
        user_items = request.user.cart.items.all()
        item = get_object_or_404(CartItem, sku=view.kwargs['cart_item_sku'])
        if not item in user_items:
            return False
        return True