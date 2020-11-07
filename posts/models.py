from django.db import models
from django.conf import settings
from authentication.models import CustomUser
from django.utils import timezone

class Post(models.Model):
    image = models.CharField(max_length=200, blank=False, default='')
    caption = models.CharField(max_length=100, blank=True, default='')
    soundcloud = models.CharField(max_length=200, blank=True, null=True, default='')
    beatport = models.CharField(max_length=200, blank=True, null=True, default='')
    bandcamp = models.CharField(max_length=200, blank=True, null=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('authentication.CustomUser', related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-timestamp'] 

class Comment(models.Model):
    comment = models.CharField(max_length=200, blank=False, null=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete=(models.CASCADE))
    post = models.ForeignKey(Post, on_delete=(models.CASCADE))

    def __str__(self):
        return f"{self.comment}"

    class Meta:
        ordering = ['-created_date']

