from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "rent_type", "price", "area", "location", "room_type"]


class detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "rent_type",
            "area",
            "location",
            "room_type",
            "maintenance_fee",
            "parking_fee",
            "description",
        ]
