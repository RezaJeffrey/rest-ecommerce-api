from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscountCodeViewSet

router = DefaultRouter()
router.register(r'discountcode', DiscountCodeViewSet, basename='discountcode')

app_name = 'dsicount'
urlpatterns = [
    path('', include(router.urls))
]
