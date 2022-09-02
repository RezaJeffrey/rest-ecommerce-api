from django.urls import path
from .views import(AllCategoriesListView, CategoryCreateView
                   )

app_name = 'categories:api:v1'
urlpatterns = [
    path('categories/', AllCategoriesListView.as_view(), name='categories'),
]