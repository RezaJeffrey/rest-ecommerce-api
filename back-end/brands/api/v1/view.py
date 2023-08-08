from brands.api.v1.serializer import BrandSerializer
from rest_framework.viewsets import ModelViewSet
from brands.models import Brand
from core.permissions import IsCustomer, IsSeller
from rest_framework import status
from rest_framework.response import Response


class BrandView(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    # def get_permissions(self):
    #     if self.action == 'create' and self.action == 'update':
    #         permission_classes = [IsSeller]
    #     else:
    #         permission_classes = [IsCustomer]
    #     return [permission() for permission in permission_classes]

    def retrieve(self, request, brand_sku=None):
        brand = Brand.objects.get(
            sku=brand_sku
        )
        serializer = self.serializer_class(instance=brand, many=False)
        response = {
            'data': serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )








