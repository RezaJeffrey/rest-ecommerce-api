from rest_framework.routers import DefaultRouter
from shops.api.v1.view import ShopView, ShopAddressView

routers = DefaultRouter()
routers.register(r'shop', ShopView, basename='shop')
routers.register(r'shop_address', ShopAddressView, basename='shop_address')


app_name = 'v1'
urlpatterns = routers.urls
