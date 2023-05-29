from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'birth_date', 'telephone', 'email', 'password', 'created_at', 'updated_at']
        depth = 5

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'birth_date', 'telephone', 'email', 'password']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'birth_date', 'telephone']

