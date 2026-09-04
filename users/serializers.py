from rest_framework import serializers
from .models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(write_only=True, style={"input_type": "password"})
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 
                  'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'username': {'required': True},
        }
       
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    # ovverride create method to handle password confirmation
    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        return User.objects.create_user(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'memberSince']