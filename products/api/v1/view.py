from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, ProductCreateSerializer, ExtraFieldSerializer
from rest_framework import permissions
from products.models import Product, ExtraFieldValue
from comments.api.v1.serializer import CreateCommentSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            serializer_class = ProductCreateSerializer
        else:
            serializer_class = ProductSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_class = []
        else:
            permission_class = [permissions.IsAuthenticated]
        return [permission() for permission in permission_class]

    def retrieve(self, request, pk=None, product_sku=None, *args, **kwargs):
        queryset = get_object_or_404(
            Product,
            pk=pk,
            sku=product_sku
        )
        serializer = self.get_serializer(instance=queryset, many=False)
        response = {
            'instance': serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )


class ExtraFieldViewSet(ModelViewSet):
    serializer_class = ExtraFieldSerializer
    queryset = ExtraFieldValue.objects.all()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_class = []
        else:
            permission_class = [permissions.IsAuthenticated]
        return [permission() for permission in permission_class]

    def create(self, request, product_sku=None):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(
                product_sku=product_sku,
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


class AddLikeProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, product_pk, product_sku):
        product = Product.objects.get(
            pk=product_pk,
            sku=product_sku
        )
        product.likes.create(
            user=request.user
        )
        response = {
            'message': 'liked'
        }
        code = status.HTTP_201_CREATED
        return Response(
            data=response,
            status=code
        )

class AddCommentProduct(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentSerializer

    def post(self, request, product_pk, product_sku):
        payload = request.data
        current_user = request.user
        product = Product.objects.get(
            pk=product_pk,
            sku=product_sku
        )
        serializer = self.serializer_class(
            data=payload,
        )
        if serializer.is_valid():
            product.comments.create(
                user=current_user,
                **serializer.validated_data
            )
            response = {
                'message': 'your comment placed successfully!',
                'comment': serializer.data
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