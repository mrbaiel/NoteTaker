from rest_framework import generics, status
from django.contrib.auth import login
from rest_framework.response import Response

from core.serializers import CreateUserSerializer, LoginSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, reauest, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        login(request=request, user=serializers.save())
        return Response(serializers.data, status=status.HTTP_201_CREATED)

