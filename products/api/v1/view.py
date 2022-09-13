from rest_framework.views import APIView
from eav.models import Attribute
from products.models import ProductPack
from .serializers import AddFieldSerializer
from rest_framework import status
from rest_framework.response import Response


class AddFieldProductPack(APIView):
    serializer_class = AddFieldSerializer
    lst = []

    def post(self, request):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            self.lst.append(serializer.data)
            response = {
                'added_fields': self.lst
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                'error': serializer.errors,
                'created_fields': self.lst
            }
            code = status.HTTP_400_BAD_REQUEST
        return Response(
            data=response,
            status=code
        )

class ProductPackCreateView(APIView):
    pass

