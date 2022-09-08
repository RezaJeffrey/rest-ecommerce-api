from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from category.models import Category
from rest_framework import status
from .serializers import CategorySerializer, CategoryCreateSerializer, CategorySearchSerializer
from rest_framework.permissions import IsAdminUser


class AllCategoriesListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        keywords = self.request.query_params.get('search')
        if keywords:
            queryset = Category.objects.filter(name__icontains=keywords)
        else:
            queryset = Category.objects.filter(parent=None).prefetch_related('child')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(instance=queryset, many=True)
        code = status.HTTP_200_OK
        return Response(serializer.data, status=code)


class CategoryCreateView(APIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAdminUser]

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

