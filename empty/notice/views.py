from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notice
from .serializers import (
    NoticeSerializer,
    NoticeCreateSerializer,
    NoticeUpdateSerializer,
)
from rest_framework import generics


class NoticeListAPIView(APIView):
    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NoticeCreateAPIView(generics.CreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "성공적으로 생성되었습니다."}, status=status.HTTP_201_CREATED)


class NoticeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return NoticeUpdateSerializer
        return NoticeCreateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "성공적으로 수정되었습니다."})
