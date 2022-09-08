from django.urls import path
from rest_framework import routers
from .views import AllCategoriesListView, CategoryCreateView

router = routers.DefaultRouter()
app_name = 'v1'

urlpatterns = [
    path('categories/', AllCategoriesListView.as_view(), name='categories'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
]

