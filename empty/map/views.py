from django.shortcuts import render
from rest_framework import generics
from .models import Room, Room_detail
from .serializers import RoomSerializer, detailSerializer


# Create your views here.


def map_view(request):
    return render(request, "kakao/map.html")


def map_apartment_view(request):
    return render(request, "kakao/map_apartment.html")


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MonthlyRoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.filter(rent_type="월세")
    serializer_class = RoomSerializer


class LeaseRoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.filter(rent_type="전세")
    serializer_class = RoomSerializer


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room_detail.objects.all()
    serializer_class = detailSerializer
    lookup_field = "pk"
