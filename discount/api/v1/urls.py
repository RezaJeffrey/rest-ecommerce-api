from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductDiscountView

router = DefaultRouter()

app_name = "discount"

urlpatterns = [
    path("discount_code/<str:product_pack_sku>/", ProductDiscountView.as_view(), name="product_discount")
] + router.urls



