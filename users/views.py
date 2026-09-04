from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        """ Dynamically assign permissions based on the action """
        if self.action == 'create':
            return [AllowAny()]  # Anyone can sign up
        return [IsAuthenticated()]  # Must be logged in to view, update, or delete profiles
    
    
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer