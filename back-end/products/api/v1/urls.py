from products.api.v1.view import (
    ProductViewSet,
    AddLikeProduct, AddCommentProduct,
    AddProductImageView
)
from extra_fields.api.v1.view import ExtraFieldViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

routers = DefaultRouter()
routers.register(r'product', ProductViewSet, basename='product')


app_name = 'products'
urlpatterns = [
    path('product/<int:product_pk>/<str:product_sku>/add_like', AddLikeProduct.as_view(), name='add_like'),
    path('product/<int:product_pk>/<str:product_sku>/add_comment', AddCommentProduct.as_view(), name='add_comment'),
    path('product/add_image', AddProductImageView.as_view(), name='add_image')
] + routers.urls


