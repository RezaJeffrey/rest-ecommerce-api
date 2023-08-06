from django.contrib.auth import get_user_model
# Third-party package imports
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# .files import
from users.api.v1.serializers import (MyTokenObtainPairSerializer, ChangePasswordSerializer, UserProfileSerializer)

# user
User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(instance=user, many=False)
        response = {
            "profile": serializer.data
        }
        code = status.HTTP_200_OK
        return Response(
            data=response,
            status=code
        )

