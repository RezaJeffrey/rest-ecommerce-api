from urllib.parse import urlparse
from urllib.parse import parse_qs

from products.models import Product
from productpacks.models import ProductPack
from extra_fields.models import ExtraFieldValue
from category.models import Category
from brands.models import Brand
from shops.models import Shop

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializer import ProductSerializer, ProductCreateSerializer, ExtraFieldSerializer
from rest_framework import permissions
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
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_queryset(self, *args, **kwargs):
        url = urlparse(self.request.get_full_path())
        queries = parse_qs(url.query)
        try:
            params = parse_qs(queries["params"][0])
        except:
            return Product.objects.all()
        category_param = params.get("categories")
        price_param = params.get("price")
        brand_param = params.get("brands")
        shop_param = params.get("shops")
        categories_ToBe_filtered = Category.objects.all().values_list("sku", flat=True)
        prices_ToBe_filtered = [0, ProductPack.objects.order_by("-price").first().price]
        brands_ToBe_filtered = Brand.objects.all().values_list("sku", flat=True)
        shops_ToBe_filtered = Shop.objects.all().values_list("sku", flat=True)
        if category_param:
            categories_ToBe_filtered = category_param[0].split(", ")
        if price_param:
            price_arr =  price_param[0].split(", ")
            if price_arr != ['0', '0']:
                prices_ToBe_filtered = price_arr
        if brand_param:
            brands_ToBe_filtered = brand_param[0].split(", ")
        if shop_param:
            shops_ToBe_filtered = shop_param[0].split(", ") 
        queryset = Product.objects.prefetch_related("paks").filter(
            category__sku__in = categories_ToBe_filtered, 
            brand__sku__in = brands_ToBe_filtered, 
            shop__sku__in = shops_ToBe_filtered, 
            paks__price__gte = prices_ToBe_filtered[0],
            paks__price__lte = prices_ToBe_filtered[1]
        ).distinct()
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            serializer_class = ProductCreateSerializer
        else:
            serializer_class = ProductSerializer
        return serializer_class


    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'get_maximum_price':
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
    
    @action(detail=False, methods=['GET'])
    def get_maximum_price(self, request):
        queryset = self.get_queryset()
        maximum_price = ProductPack.objects.filter(product__in = queryset).order_by("-price").first().price
        return Response(
            data = {
                "maximum_price": maximum_price
            },
            status=status.HTTP_200_OK
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
