from django.urls import path, include
from .views import (
    ProductPackViewSet,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'productpack', ProductPackViewSet, basename='productpack')


app_name = 'product_pack'
urlpatterns = [
    # path("create_pack/", ProductPackViewSet.as_view(), name="create_pack"),
    # path("value_list/<str:product_sku>/", ValueList.as_view(), name='value_list'),
    path('', include(router.urls))
]

