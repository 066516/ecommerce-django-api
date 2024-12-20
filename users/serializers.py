# users/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # If you're using a custom user model, replace with `from .models import User`
        fields = ['id', 'username', 'email', 'password']
