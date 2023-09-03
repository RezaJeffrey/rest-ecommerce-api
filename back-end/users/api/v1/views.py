from django.contrib.auth import get_user_model
# Third-party package imports
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
# .files import
from users.api.v1.serializers import (MyTokenObtainPairSerializer, ChangePasswordSerializer, UserProfileSerializer, UserRegisterationSerializer)
from django.contrib.auth import authenticate

# user
User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    authentication_classes = ([])
    serializer_class = UserRegisterationSerializer
    def create(self, request, *args, **kwargs):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            response = {
                "message": "user registered successfully!",
                "data": serializer.data
            }
            code = status.HTTP_201_CREATED
        else:
            response = {
                "message": "something went wrong!",
                "error": serializer.errors
            }
            code = status.HTTP_406_NOT_ACCEPTABLE
        return Response(
            data=response,
            status=code
        )


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

