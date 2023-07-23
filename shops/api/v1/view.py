from rest_framework.viewsets import ModelViewSet
from shops.api.v1.serializer import ShopSerializer, ShopAddressSerializer, ShopStafSerializer
from core.permissions import IsCustomer, IsSeller
from shops.models import Shop, ShopAddress, ShopStaf


class ShopView(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    def get_permissions(self):
        if self.action == 'create' and self.action == 'update':
            permission_classes = [IsSeller]
        else:
            permission_classes = [IsCustomer]
        return [permission() for permission in permission_classes]


class ShopAddressView(ModelViewSet):
    serializer_class = ShopAddressSerializer
    queryset = ShopAddress.objects.all()

    def get_permissions(self):
        if self.action == 'create' and self.action == 'update':
            permission_classes = [IsSeller]
        else:
            permission_classes = [IsCustomer]
        return [permission() for permission in permission_classes]







