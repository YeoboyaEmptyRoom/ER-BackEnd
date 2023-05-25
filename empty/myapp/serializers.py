# serializers.py
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    email = serializers.EmailField()


class VerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField()
