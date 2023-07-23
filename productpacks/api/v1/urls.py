from django.urls import path, include
from .views import (
    ProductPackViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'productpack', ProductPackViewSet, basename='productpack')

app_name = 'product_pack'
urlpatterns = [
    path('', include(router.urls))
]

