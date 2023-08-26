from rest_framework.permissions import BasePermission
from productpacks.models import ProductPack
from core.permissions import NotAllowed, Allowed

class IsSellerOfProductPack(BasePermission):
    def has_permission(self, request, view):
        product_pack = ProductPack.objects.get(sku=view.kwargs["product_pack_sku"])
        pack_shop = product_pack.shop
        pack_shopstafs = pack_shop.shopstafs.all()
        user = request.user
        user_shopstafs = user.shopstafs.all()
        intersection = pack_shopstafs & user_shopstafs
        if not pack_shopstafs or not user_shopstafs or not intersection:
            return False
        else:
            return True 