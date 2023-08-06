from django.urls import path
from carts.api.v1.views import (
    CartView, CartItemLView, CartItemCView,
    CartItemRDView, CartCreateView
)


app_name = 'v1'
urlpatterns = [
    path('cart/create/', CartCreateView.as_view(), name='create_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart_item/', CartItemLView.as_view(), name='itemL'),
    path('cart_item/<str:product_pack_sku>/', CartItemCView.as_view(), name='itemC'),
    path('cart_item_detail/<str:cart_item_sku>', CartItemRDView.as_view(), name='itemRUD')
]








