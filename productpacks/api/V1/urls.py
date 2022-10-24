from django.urls import path
from .views import CreatePack

app_name = 'product_pack'
urlpatterns = [
    path("create_pack/<str:product_sku>", CreatePack.as_view(), name="create_pack")
]





