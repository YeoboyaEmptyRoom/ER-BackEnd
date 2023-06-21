from rest_framework import serializers
from .models import Room, Room_detail


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "rent_type", "price", "area", "location", "room_type"]


class detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_detail
        fields = [
            "id",
            "rent_type",
            "area",
            "location",
            "floor",
            "size",
            "room_type",
            "maintenance_fee",
            "parking_fee",
            "description",
        ]
