from django.urls import path, include
from django.http import HttpResponse
from .views import (
    map_view,
    map_apartment_view,
    RoomListAPIView,
    MonthlyRoomListAPIView,
    LeaseRoomListAPIView,
    RoomDetailAPIView,
)

urlpatterns = [
    path("check-main", lambda request: HttpResponse("확인")),
    path("map/", map_view, name="map"),
    path("map_apartment/", map_apartment_view, name="apart"),
    # path("map/apart",),
    path("rooms/", RoomListAPIView.as_view(), name="room-list"),
    path("rooms/monthly/", MonthlyRoomListAPIView.as_view(), name="monthly-room-list"),
    path("rooms/lease/", LeaseRoomListAPIView.as_view(), name="lease-room-list"),
    # 상세 페이지
    path("room_detail/<int:pk>/", RoomDetailAPIView.as_view(), name="room_detail"),
]
