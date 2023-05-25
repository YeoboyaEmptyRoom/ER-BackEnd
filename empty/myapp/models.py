# models.py
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    # 필요한 다른 필드들
    USERNAME_FIELD = "email"
