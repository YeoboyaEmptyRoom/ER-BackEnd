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
