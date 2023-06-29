from django.urls import path
from .views import NoticeListAPIView, NoticeCreateAPIView, NoticeDetailAPIView

app_name = "notices"

urlpatterns = [
    path("list/", NoticeListAPIView.as_view(), name="notice_list"),
    path("create/", NoticeCreateAPIView.as_view(), name="notice-create"),
    path("list/<int:pk>/", NoticeDetailAPIView.as_view(), name="notice-detail"),
]
