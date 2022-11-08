from rest_framework.routers import DefaultRouter
from extra_fields.api.v1.view import ExtraFieldViewSet
from django.urls import path


routers = DefaultRouter()
routers.register(r'extra_field', ExtraFieldViewSet, basename='extra_field')


app_name = 'extra_fields'
urlpatterns = [
    path('extra_field/create/<str:product_sku>', ExtraFieldViewSet.as_view({'post': 'create'}), name='create_field'),
] + routers.urls











