from .serializers import ProductDiscountSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from core.permissions import IsSeller
from discount.permissions import IsSellerOfProductPack
from discount.models import Blacklist, ProductDiscount
from productpacks.models import ProductPack
from django.shortcuts import get_object_or_404


class ProductListAndCreateDiscountView(ListCreateAPIView):
    # permission_classes = [IsSeller, IsSellerOfProductPack]
    serializer_class = ProductDiscountSerializer

    def list(self, request, product_pack_sku):
        product_pack = get_object_or_404(ProductPack, sku=product_pack_sku)
        discount_codes = product_pack.product_discounts.filter(black_list=None)
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


class ProductRetrieveUpdateDestroyDiscountView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsSeller, IsSellerOfProductPack]
    serializer_class = ProductDiscountSerializer

    def retrieve(self, request, *args, **kwargs):
        discount_code = get_object_or_404(ProductDiscount, sku=kwargs["discount_code_sku"])
        serializer = self.serializer_class(instance=discount_code, many=False)
        response = {
            "discount_code": serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )

    def delete(self, request, *args, **kwargs):
        product_discount_code = ProductDiscount.objects.get(sku=kwargs["discount_code_sku"])
        try:
            black_list = Blacklist.objects.get(name="discount_black_list", discount=product_discount_code)
        except:
            black_list = Blacklist(name="discount_black_list", content_object=product_discount_code) 
            black_list.save()
        response = {
            "message": "destroyed succefully!"
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )
        