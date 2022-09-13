from products.api.v1.view import AddFieldProductPack
from django.urls import path


app_name = 'V1'
urlpatterns = [
    path('add_field', AddFieldProductPack.as_view(), name='add_field')
]

