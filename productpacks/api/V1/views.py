from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import (
    ProductPackCreateSerializer,
    ValueListSerializer,
    AddValueToPackSerializer
)
from rest_framework.response import Response
from rest_framework import status
from products.models import Product


class CreatePack(APIView):
    serializer_class = ProductPackCreateSerializer

    def post(self, request, product_sku=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(product_sku=product_sku)
            response = {
                "data": serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "errors": serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(
            data=response,
            status=code
        )


class AddValueToPack(CreateAPIView):
    serializer_class = AddValueToPackSerializer

    def post(self, request, product_pack_sku, value_sku):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.create(
                product_pack_sku=product_pack_sku,
                value_sku=value_sku
            )
            response = {
                'massage': 'value added!',
                'data': serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                'errors': serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(
            data=response,
            status=code
        )


class ValueList(ListAPIView):
    serializer_class = ValueListSerializer

    def get(self, request, product_sku=None):
        product = Product.objects.get(
            sku=product_sku
        )
        extra_fields = product.extra_fields.all()
        serializer = self.serializer_class(
            instance=extra_fields,
            many=True
        )
        response = {
            'list': serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )
