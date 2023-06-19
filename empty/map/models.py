from django.db import models


# Create your models here.
class Room(models.Model):
    rent_type = models.CharField(max_length=50, null=True)  # 전세, 월세 등
    price = models.CharField(max_length=50, null=True)  # 가격
    area = models.FloatField(null=True)  # 면적
    location = models.CharField(max_length=100, null=True)  # 위치
    room_type = models.CharField(max_length=50, null=True)  # 원룸, 아파트 등

    def __str__(self):
        return self.location


class Room_detail(models.Model):
    rent_type = models.CharField(max_length=50)  # 전세, 월세 등
    area = models.FloatField()  # 면적
    location = models.CharField(max_length=100)  # 위치
    room_type = models.CharField(max_length=50)  # 원룸, 아파트 등
    maintenance_fee = models.IntegerField(null=True, blank=True)  # 관리비 (추가된 필드)
    parking_fee = models.IntegerField(null=True, blank=True)  # 주차비 (추가된 필드)
    description = models.TextField(null=True, blank=True)  # 상세 설명 (추가된 필드)
    floor = models.IntegerField(null=True, blank=True)  # 층수 (추가된 필드)
    size = models.FloatField(null=True, blank=True)  # 평수 (추가된 필드)

    def __str__(self):
        return self.location
