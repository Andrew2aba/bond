from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer, RegisterUserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    register_serializer_class = RegisterUserSerializer  # Serializer for registration
    
    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterUserSerializer
        return UserSerializer
    
    def get_permissions(self):
        """ Dynamically assign permissions based on the action """
        if self.action == 'create':
            return [AllowAny()]  # Anyone can sign up
        return [IsAuthenticated()]  # Must be logged in to view, update, or delete profiles
    
    def create(self, request, *args, **kwargs):
        """ Custom action for user registration """
        serializer = self.register_serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh_token = RefreshToken.for_user(user)
            return Response({
                "message": "User registered successfully.",
                "access": str(refresh_token.access_token),   # Expiring credentials for headers
                "refresh": str(refresh_token),        # Refresh token
                "user": UserSerializer(user).data     # Public profile info
            }, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# users/views.py
class LoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    
    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.user
            refresh_token = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful.",
                "access": str(refresh_token.access_token),
                "refresh": str(refresh_token),
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer