from products.api.v1.view import AddFieldProductPack
from django.urls import path


app_name = 'V1'
url_patterns = [
    path('add_field', AddFieldProductPack.as_view(), name='add_field')
]

