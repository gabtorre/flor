from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.CharField(blank=True, null=True, max_length=200)
    cover = models.CharField(blank=True, null=True, max_length=200)