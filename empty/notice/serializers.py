from rest_framework import serializers
from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ("title", "content", "created_at")


class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ("title", "content")


class NoticeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ("title", "content")
