from .serializers import ProductDiscountSerializer, ProductDiscountCreateSerializer, ProductDiscountUpdateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from core.permissions import IsSeller
from discount.permissions import IsSellerOfProductPack
from discount.models import Blacklist, ProductDiscount
from productpacks.models import ProductPack
from django.shortcuts import get_object_or_404


class ProductListAndCreateDiscountView(ListCreateAPIView):
    permission_classes = [IsSeller, IsSellerOfProductPack]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return ProductDiscountCreateSerializer
        else:
            return ProductDiscountSerializer

    def list(self, request, product_pack_sku):
        product_pack = get_object_or_404(ProductPack, sku=product_pack_sku)
        discount_codes = product_pack.product_discounts.filter(black_list=None)
        serializer = self.get_serializer_class()
        serializer = serializer(instance=discount_codes, many = True)
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
        serializer = self.get_serializer_class()
        serializer = serializer(data=payload)
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
    permission_classes = [IsSeller, IsSellerOfProductPack]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return ProductDiscountSerializer
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return ProductDiscountUpdateSerializer

    def get_object(self, *args, **kwargs):
        return get_object_or_404(ProductDiscount, sku=kwargs["discount_code_sku"])

    def retrieve(self, request, *args, **kwargs):
        discount_code = self.get_object(*args, **kwargs)
        serializer = self.get_serializer_class()
        serializer = serializer(instance=discount_code, many=False)
        response = {
            "discount_code": serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )

    def delete(self, request, *args, **kwargs):
        product_discount_code = self.get_object(*args, **kwargs)
        product_discount_code.black_list.create(
            name="product_discount_blacklist"
        )
        response = {
            "message": "destroyed succefully!"
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )
    
    def update(self, request, *args, **kwargs):
        payload = request.data
        product_discount_code = ProductDiscount.objects.get(sku=kwargs["discount_code_sku"])
        serializer = self.get_serializer_class()
        serializer = serializer(data=payload)
        if serializer.is_valid():
            serializer.update(product_discount_code, serializer.validated_data)
            response = {
                "message": "updated successfully!",
                "data": serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "message": "something went wrong!",
                "error": serializer.errors
            }
            code = status.HTTP_400_BAD_REQUEST
        return Response(
            data=response,
            status=code
        )
        