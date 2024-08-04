from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class CustomTokenObtainPairView(generics.GenericAPIView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    