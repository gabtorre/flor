from django.db import models

class Post(models.Model):
    image = models.CharField(max_length=100, blank=False, default='')
    caption = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp'] 
