from rest_framework import generics, status, permissions
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.models import User
from core.serializers import CreateUserSerializer, LoginSerializer, ProfileSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        login(request=request, user=serializers.save())
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
