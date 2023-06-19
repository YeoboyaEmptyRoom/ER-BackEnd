from django.shortcuts import render
from rest_framework import generics
from .models import Room, Room_detail
from .serializers import RoomSerializer


# Create your views here.


def map_view(request):
    return render(request, "kakao/map.html")


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MonthlyRoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.filter(rent_type="월세")
    serializer_class = RoomSerializer


class LeaseRoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.filter(rent_type="전세")
    serializer_class = RoomSerializer


# class detailAPIView(generics.ListAPIView):
