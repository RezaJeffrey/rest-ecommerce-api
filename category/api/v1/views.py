from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from category.models import Category
from rest_framework import status
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser


class AllCategoriesListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(instance=queryset, many=True)
        response = {
            'list': serializer.data
        }
        code = status.HTTP_200_OK
        return Response(data=response, status=code)


class CategoryCreateView(APIView):
    serializer_class = CategorySerializer

    def post(self, request):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.create(**validated_data)
            response = {
                'message': 'new category created',
                'category data': validated_data
            }
            code = status.HTTP_201_CREATED

        else:
            response = {
                'errors': serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(data=response, status=code)

