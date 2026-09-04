from rest_framework import viewsets, status
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        """ Dynamically assign permissions based on the action """
        if self.action == 'create':
            return [AllowAny()]  # Anyone can sign up
        return [IsAuthenticated()]  # Must be logged in to view, update, or delete profiles
    
    def create(self, request, *args, **kwargs):
        """ Optional override to customize the registration response payload """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "message": "User registered successfully!",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }, status=status.HTTP_201_CREATED)


    
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer