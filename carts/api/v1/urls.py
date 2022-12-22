from django.urls import path, include
from carts.api.v1 import views
from rest_framework.routers import DefaultRouter

cart_router = DefaultRouter()
item_router = DefaultRouter()
cart_router.register(r'cart', views.CartView, basename='cart')
item_router.register(r'cart_item', views.CartItemView, basename='cart_item')

app_name = 'carts'
urlpatterns = [
    path('', include(cart_router.urls)),
    path('', include(item_router.urls))
]
