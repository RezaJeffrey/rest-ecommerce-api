from rest_framework.viewsets import ModelViewSet
from extra_fields.models import ExtraFieldValue, ExtraFieldName
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from extra_fields.api.v1.serializer import ExtraFieldSerializer, ExtraFieldNameSerializer
from core.permissions import IsSeller
from rest_framework.decorators import action


class ExtraFieldNameViewSet(ModelViewSet):
    serializer_class = ExtraFieldNameSerializer
    queryset = ExtraFieldName.objects.all()
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_class = []
        elif self.request.user.is_superuser:
            permission_class = []
        else:
            permission_class = [IsSeller]
        return [permission() for permission in permission_class]

    def create(self, request):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(
                validated_data=serializer.validated_data
            )
            response = {
                "data": serializer.data,
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "errors": serializer.errors
            }
            code = status.HTTP_400_BAD_REQUEST

        return Response(data=response, status=code)


class ExtraFieldViewSet(ModelViewSet):
    serializer_class = ExtraFieldSerializer
    queryset = ExtraFieldValue.objects.all()
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_class = []
        else:
            permission_class = [permissions.IsAuthenticated]
        return [permission() for permission in permission_class]

    def create(self, request):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(
                **serializer.validated_data
            )
            response = {
                'field name': serializer.data,
                'message': 'created successfully!'
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                'error': serializer.errors
            }
            code = status.HTTP_400_BAD_REQUEST
        return Response(
            data=response,
            status=code
        )
