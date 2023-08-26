from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer, ProductCreateSerializer, ExtraFieldSerializer
from rest_framework import permissions
from products.models import Product
from extra_fields.models import ExtraFieldValue
from comments.api.v1.serializer import CreateCommentSerializer, CommentSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializer import ProductImageCreateSerializer
from core.permissions import IsSeller


# TODO [BUG] drf-yasg occurs to bug cause of this viewset and most probably the serializer
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

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

    def retrieve(self, request, *args, **kwargs):
        queryset = get_object_or_404(
            Product,
            sku=kwargs['sku']
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

class AddProductImageView(generics.CreateAPIView):
    permission_classes = [IsSeller]
    serializer_class = ProductImageCreateSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            response = {
                "message": "image added successfully!",
                "data": serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "message": "something went wrong!",
                "error": serializer.errors
            }
            code = status.HTTP_403_FORBIDDEN
        return Response(data=response, status=code)

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
