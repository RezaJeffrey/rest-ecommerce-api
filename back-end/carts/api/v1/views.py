from rest_framework.generics import (
    RetrieveDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)
from carts.models import Cart, CartItem
from carts.api.v1.serializers import(
    CartSerializer, CartCreateSerializer,
    CartItemSerializer, CartItemCreateSerializer
)
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from carts.permission import IsCartBelongsToUser, IsUserDoesNotHaveCart


class CartCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUserDoesNotHaveCart]
    serializer_class = CartCreateSerializer

    def create(self, request):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        user = request.user
        if serializer.is_valid():
            serializer.create(
                user=user,
                validated_data=serializer.validated_data
            )
            response = {
                'data': serializer.data,
                'message': 'successfully!'
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                'error': serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(
            data=response,
            status=code
        )


class CartView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        queryset = get_object_or_404(
            Cart,
            user=user
        )
        return queryset

    def retrieve(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.serializer_class(instance=cart, many=False)
        response = {
            'data': serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )


class CartItemLView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
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


class CartItemCView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = CartItemCreateSerializer

    def get_serializer_context(self, *args, **kwargs):
        product_pack_sku = self.kwargs["product_pack_sku"]
        context = super(CartItemCView, self).get_serializer_context()
        context.update({"product_pack_sku": product_pack_sku})
        return context

    def create(self, request, product_pack_sku):
        payload = request.data
        serializer = self.serializer_class(data=payload, context=self.get_serializer_context())
        user = request.user
        cart_sku = user.cart.sku
        if serializer.is_valid():
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

# TO DO
class CartItemRDView(RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer
    lookup_field = 'sku'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CartItem, sku=kwargs["cart_item_sku"])

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object(*args, **kwargs)
        serializer = self.serializer_class(instance=queryset, many=False)
        return Response(
            data={
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object(*args, **kwargs)
        queryset.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
