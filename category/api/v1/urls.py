from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
app_name = 'v1'

router.register(r'category', CategoryViewSet)
urlpatterns = router.urls
