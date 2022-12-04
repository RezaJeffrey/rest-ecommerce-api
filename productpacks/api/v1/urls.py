from django.urls import path
from .views import (
    CreatePack, AddValueToPack,
    ValueList, UpdateValue
)

app_name = 'product_pack'
urlpatterns = [
    path("create_pack/<str:product_sku>", CreatePack.as_view(), name="create_pack"),
    path("value_list/<str:product_sku>", ValueList.as_view(), name='value_list'),
    path("add_value/<str:product_pack_sku>/<str:value_sku>", AddValueToPack.as_view(), name='add_value_to_pack'),
    path("update_value/<str:product_pack_sku>/<str:value_sku>", UpdateValue.as_view(), name='update_value')
]





