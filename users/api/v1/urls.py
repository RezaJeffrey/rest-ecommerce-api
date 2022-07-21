from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.api.v1.views import MyTokenObtainPairView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh'),
]