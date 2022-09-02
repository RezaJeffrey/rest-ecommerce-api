from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.api.v1.views import (MyTokenObtainPairView, ChangePasswordView)


app_name = 'users:api:v1'
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
]
