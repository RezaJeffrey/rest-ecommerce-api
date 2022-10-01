from .view import ProductViewSet, ExtraFieldViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

routers = DefaultRouter()
routers.register(r'product', ProductViewSet, basename='product')
routers.register(r'extra_field', ExtraFieldViewSet, basename='extra_field')

app_name = 'products'
urlpatterns = [
    path('extra_field/create/<str:product_sku>', ExtraFieldViewSet.as_view({'post': 'create'}), name='create_field')
] + routers.urls


