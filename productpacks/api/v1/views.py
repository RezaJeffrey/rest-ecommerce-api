from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from core.permissions import IsSeller
from shops.models import ShopStaf
from .serializers import (
    ProductPackCreateSerializer,
    UpdateValueSerializer, ListProductPacksSerializer
)
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from productpacks.models import ProductPack


class ProductPackViewSet(ModelViewSet):
    queryset = ProductPack.objects.all()
    lookup_url_kwarg = 'sku'
    lookup_field = 'sku'
    # permission_classes = [IsSeller]

    # def get_permissions(self):
    #     pass

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return ProductPackCreateSerializer
        else:
            return ListProductPacksSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.queryset = ProductPack.objects.all()

        else:
            self.queryset = product_packs = ProductPack.objects.filter(
                product__shop__shopstaf=self.request.user
            )
        return self.queryset

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(
                validated_data=serializer.validated_data
            )
            response = {
                "data": serializer.data,
                "message": 'successfully!'
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "errors": serializer.errors
            }
            code = status.HTTP_400_BAD_REQUEST
        return Response(
            data=response,
            status=code
        )

    def update(self, request, sku=None):
        item = get_object_or_404(self.queryset, sku=sku)
        serializer = self.get_serializer(item)
        serializer.update(
            validated_data=serializer.validated_data
        )
        response = {
            "data": serializer.data,
            "message": "updated"
        }
        code = status.HTTP_201_CREATED

        return Response(
            data=response,
            status=code
        )

    def list(self, request):
        queryset = self.queryset.order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        response = {
            "data": serializer.data
        }
        code = status.HTTP_200_OK

        return Response(
            data=response,
            status=code
        )




