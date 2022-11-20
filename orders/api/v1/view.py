from rest_framework.viewsets import ModelViewSet
from orders.api.v1.serializers import OrderAdminSerializer, OrderSerializer, OrderCreateUpdateSerializer
from orders.models import Order
from rest_framework import status
from rest_framework.response import Response


class OrderView(ModelViewSet):
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(
            user=user
        )
        return queryset

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            serializer_class = OrderCreateUpdateSerializer
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



