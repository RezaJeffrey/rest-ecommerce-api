from rest_framework.routers import DefaultRouter
from brands.api.v1.view import BrandView
from django.urls import path


routers = DefaultRouter()

routers.register(r'brand', BrandView, basename='brand')


app_name = 'v1'
urlpatterns = [
    path('brand/<str:brand_sku>', BrandView.as_view({'get': 'retrieve'}), name='brand_detail')
] + routers.urls





