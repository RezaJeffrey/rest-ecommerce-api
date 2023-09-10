from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from users.api.v1.views import (
    MyTokenObtainPairView, ChangePasswordView, 
    UserProfileView, UserRegisterView,
    AddUserProfileImageView
)


app_name = 'users'
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("add_user_profile_image/", AddUserProfileImageView.as_view(), name="add_user_profile_image")
]
