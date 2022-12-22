from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from discount.api.v1.serializers import DiscountCodeSerializer
from discount.models import DiscountCode


class DiscountCodeViewSet(ModelViewSet):
    serializer_class = DiscountCodeSerializer
    queryset = DiscountCode.objects.all()
    lookup_url_kwarg = 'sku'
    lookup_field = 'sku'

    # TODO permissions
    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(
                user=user,
                **serializer.validated_data
            )
            response = {
                "data": serializer.data,
                "message": "copoun created"
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "errors": serializer.errors
            }
            code = status.HTTP_400_BAD_REQUEST
        return Response(data=response, status=code)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(shop__shopstaf__user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
