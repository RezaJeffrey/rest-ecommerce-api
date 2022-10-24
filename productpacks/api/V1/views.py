from rest_framework.views import APIView
from .serializers import ProductPackSerializer
from rest_framework.response import Response
from rest_framework import status


class CreatePack(APIView):
    serializer_class = ProductPackSerializer

    def get(self, request, product_sku=None):
        context = self.get_serializer_context()
        context.update({"product_sku": product_sku})
        serializer = self.serializer_class(
            context=context
        )
        return Response()

    def post(self, request):
        payload = self.request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(**serializer.validated_data)
            response = {
                "data": serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "errors": serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        Response(
            data=response,
            status=code
        )
