from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from carts.models import Cart, CartItem
from carts.api.v1.serializers import (
    CartItemSerializer, CartItemCreateSerializer, CartSerializer
)
from rest_framework import status
from rest_framework.response import Response

from productpacks.models import ProductPack


class CartItemView(ModelViewSet):
    queryset = CartItem.objects.all()
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(
            cart__user=user
        )
        return queryset

    def get_serializer_class(self):
        if self.action == 'get':
            serializer = CartItemSerializer
        else:
            serializer = CartItemCreateSerializer
        return serializer

    def create(self, request):
        payload = request.data
        user = request.user
        cart_sku = user.cart.sku
        serializer = self.get_serializer(data=payload)

        if serializer.is_valid():
            item_pk = serializer.validated_data.get('item').pk
            product_pack_sku = ProductPack.objects.get(pk=item_pk).sku
            serializer.create(
                cart_sku=cart_sku,
                product_pack_sku=product_pack_sku,
                validated_data=serializer.validated_data
            )
            response = {
                'message': 'Item added successfully!',
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


class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def list(self, request, *args, **kwargs):
        cart = self.get_queryset().filter(user=request.user).first()
        query = CartItem.objects.filter(cart__user=request.user)
        context = {
            'items': query,
            'cart_totol_price': cart.cart_total_price,
        }
        serializer = self.get_serializer(context)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
