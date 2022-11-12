from django.urls import path
from carts.api.v1.views import CartView, CartItemLCView, CartItemRUDView


app_name = 'v1'
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart_item/<str:cart_sku>/<str:product_pack_sku>/', CartItemLCView.as_view(), name='itemLC'),
]








