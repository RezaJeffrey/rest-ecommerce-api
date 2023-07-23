from .serializers import DiscountCodeSerializer, ProductDiscountSerializer
from rest_framework.viewsets import ModelViewSet
from discount.models import DiscountCode
from core.permissions import IsSeller


class DiscountCodeViewSet(ModelViewSet):
    queryset = DiscountCode.objects.all()
    permission_classes = [IsSeller]
    serializer_class = DiscountCodeSerializer

