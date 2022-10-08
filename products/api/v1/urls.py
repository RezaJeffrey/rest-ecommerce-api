from .view import (
    ProductViewSet, ExtraFieldViewSet,
    LikeProduct
)
from rest_framework.routers import DefaultRouter
from django.urls import path

routers = DefaultRouter()
routers.register(r'product', ProductViewSet, basename='product')
routers.register(r'extra_field', ExtraFieldViewSet, basename='extra_field')

app_name = 'products'
urlpatterns = [
    path('extra_field/create/<str:product_sku>', ExtraFieldViewSet.as_view({'post': 'create'}), name='create_field'),
    path('product/<int:pk>/<str:product_sku>', ProductViewSet.as_view({'get': 'retrieve'}), name='retrieve_product'),
    path('product/<int:product_pk>/<str:product_sku>/add_like', LikeProduct.as_view(), name='add_like')
] + routers.urls


