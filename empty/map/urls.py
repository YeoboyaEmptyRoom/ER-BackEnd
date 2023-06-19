from django.urls import path, include
from django.http import HttpResponse
from .views import (
    map_view,
    RoomListAPIView,
    MonthlyRoomListAPIView,
    LeaseRoomListAPIView,
)

urlpatterns = [
    path("check-main", lambda request: HttpResponse("확인")),
    path("map/", map_view, name="map"),
    # path("map/apart",),
    path("rooms/", RoomListAPIView.as_view(), name="room-list"),
    path("rooms/monthly/", MonthlyRoomListAPIView.as_view(), name="monthly-room-list"),
    path("rooms/lease/", LeaseRoomListAPIView.as_view(), name="lease-room-list"),
]
