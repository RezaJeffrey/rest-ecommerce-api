from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from address.models import Address
from address.api.v1.serializers import AddressSerializer
from rest_framework.response import Response
from rest_framework import status


class AddressView(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        payload = request.data
        user = request.user
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(
                user=user,
                validated_data=serializer.validated_data
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
