from django.db import models
from django.conf import settings
from authentication.models import CustomUser

class Post(models.Model):
    image = models.CharField(max_length=100, blank=False, default='')
    caption = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('authentication.CustomUser', related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-timestamp'] 
