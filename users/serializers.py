from rest_framework import serializers
from .models import User
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 
                  'email', 'date_joined', 'is_staff']
        read_only_fields = ['id', 'is_staff', 'date_joined']

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"},
                                     min_length=8)
    confirm_password = serializers.CharField(write_only=True, style={"input_type": "password"})
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 
                  'email', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    # creates new row after validating the data and removing confirm_password
    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        return User.objects.create_user(**validated_data)
    
    def isExistingUser(self, email):
        """ Check if a user with the given email already exists. """
        return User.objects.filter(email=email).exists()
    
class LoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)   # verifies password, returns access + refresh
        data['user'] = UserSerializer(self.user).data
        return data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'memberSince']