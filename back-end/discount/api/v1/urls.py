from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductListAndCreateDiscountView, ProductRetrieveUpdateDestroyDiscountView

router = DefaultRouter()

app_name = "discount"

urlpatterns = [
    path("discount_code/<str:product_pack_sku>/", ProductListAndCreateDiscountView.as_view(), name="product_discount_lc"),
    path("discount_code/<str:product_pack_sku>/<str:discount_code_sku>/", ProductRetrieveUpdateDestroyDiscountView.as_view(), name="product_discount_rud")
] + router.urls



