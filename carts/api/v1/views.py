from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    RetrieveAPIView
)
from carts.models import Cart, CartItem
from carts.api.v1.serializers import CartSerializer, CartItemSerializer
from rest_framework import status
from rest_framework.response import Response


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        queryset = Cart.objects.get(
            user=user
        )
        return queryset

    def retrieve(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.serializer_class(instance=cart, many=False)
        response = {
            serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )


class CartItemLCView(ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CartItem.objects.filter(
            cart__user=user
        )
        return queryset

    def list(self, request, *args, **kwargs):
        items = self.get_queryset()
        serializer = self.serializer_class(
            instance=items,
            many=True
        )
        response = {
            'data': serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )

    def create(self, request, cart_sku, product_pack_sku):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(
                cart_sku=cart_sku,
                product_pack_sku=product_pack_sku,
                **serializer.validated_data
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


class CartItemRUDView(RetrieveUpdateDestroyAPIView):
    pass






