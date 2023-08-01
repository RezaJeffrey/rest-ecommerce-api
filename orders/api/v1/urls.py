from rest_framework.routers import DefaultRouter
from orders.api.v1.view import OrderView
from django.urls import path

router = DefaultRouter()
router.register(r'order', OrderView, basename='order')

app_name = 'order'
urlpatterns = [
    path('set_status/<str:cart_sku>/', OrderView.as_view({'put': 'set_status'}), name='set_status')
] + router.urls
