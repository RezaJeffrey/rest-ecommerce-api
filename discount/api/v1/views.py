from .serializers import DiscountCodeSerializer, ProductDiscountSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from core.permissions import IsSeller
from discount.permissions import IsSellerOfProductPack
from productpacks.models import ProductPack
from django.shortcuts import get_object_or_404



class ProductDiscountView(ListCreateAPIView):
    permission_classes = [IsSeller, IsSellerOfProductPack]
    serializer_class = ProductDiscountSerializer

    def list(self, request, product_pack_sku):
        product_pack = get_object_or_404(ProductPack, sku=product_pack_sku)
        discount_codes = product_pack.product_discounts.all()
        serializer = self.serializer_class(instance=discount_codes, many = True)
        response = {
            "data": serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )
    

    def create(self, request, *args, **kwargs):
        product_pack_sku = kwargs["product_pack_sku"]
        product_pack = ProductPack.objects.get(sku=product_pack_sku)
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(validated_data = serializer.validated_data, product_pack = product_pack)
            response = {
                "message": "new discount code created!",
                "data": serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "message": "something went wrong!",
                "error": serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(
            data=response,
            status=code
        )
        

