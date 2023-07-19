from rest_framework.viewsets import ModelViewSet
from orders.api.v1.serializers import OrderStatusSerializer, OrderSerializer, OrderCreateUpdateSerializer
from orders.models import Order
from carts.models import Cart
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from core.permissions import IsSeller
from rest_framework.permissions import IsAuthenticated


class OrderView(ModelViewSet):
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_permissions(self):
        if self.action == 'set_status':
            permission_class = [IsSeller]
        else:
            permission_class = [IsAuthenticated]
        return [permission() for permission in permission_class]

    def get_queryset(self, cart_sku=None):
        user = self.request.user
        if self.action == 'set_status':
            cart = get_object_or_404(Cart, sku=cart_sku)
            queryset = cart.order.status
        else:
            queryset = Order.objects.filter(
                user=user
            )
        return queryset

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            serializer_class = OrderCreateUpdateSerializer
        elif self.action == 'set_status':
            serializer_class = OrderStatusSerializer
        else:
            serializer_class = OrderSerializer
        return serializer_class

    def get_serializer_context(self):
        context = super(OrderView, self).get_serializer_context()
        user = self.request.user
        context.update({'user': user})
        return context

    def create(self, request):
        payload = request.data
        serializer = self.get_serializer(data=payload)
        user = self.request.user
        if serializer.is_valid():
            serializer.create(
                user=user,
                **serializer.validated_data
            )
            response = {
                'message': 'successfully!',
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

    @action(methods=['put'], detail=True)
    def set_status(self, request, cart_sku=None):
        payload = request.data
        queryset = self.get_queryset(cart_sku=cart_sku)
        serializer = self.get_serializer(queryset, data=payload)
        if serializer.is_valid():
            serializer.update(
                instance=queryset,
                **serializer.validated_data
            )
            response = {
                'message': 'status updated successfully!',
                'data': serializer.data
            }
            code = status.HTTP_202_ACCEPTED
        else:
            response = {
                'error': serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(
            data=response,
            status=code
        )




