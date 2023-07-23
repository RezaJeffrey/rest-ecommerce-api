from .serializers import DiscountCodeSerializer, ProductDiscountSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from discount.models import DiscountCode
from core.permissions import IsSeller
from productpacks.models import ProductPack
from django.shortcuts import get_object_or_404


class DiscountCodeViewSet(ModelViewSet):
    queryset = DiscountCode.objects.all()
    permission_classes = [IsSeller]
    serializer_class = DiscountCodeSerializer


class ProductDiscountView(ListCreateAPIView):
    permission_classes = [IsSeller]
    serializer_class = ProductDiscountSerializer

    def list(self, request, product_pack_pk):
        # TO DO only seller who owns the shop of product can see the list of discount codes
        product_pack = get_object_or_404(ProductPack, pk=product_pack_pk)
        user = request.user
        

