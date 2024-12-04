from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    telegram_id = models.CharField(unique=True, verbose_name="ID Телеграмм", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
