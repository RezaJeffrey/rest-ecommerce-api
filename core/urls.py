from django.contrib import admin
from django.urls import path, include
from users.api.v1.serializers import MyTokenObtainPairSerializer
from users.api.v1.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


router = DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include(router.urls)),
    # path('api/', include('users.api.v1.urls')),
]

