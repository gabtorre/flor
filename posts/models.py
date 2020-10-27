from django.db import models

class Post(models.Model):
    image = models.CharField(max_length=100, blank=False, default='')
    caption = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-timestamp'] 
