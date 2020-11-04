from django.db import models
from authentication.models import CustomUser

# Create your models here.

class UserFollowing(models.Model):
    user_id = models.ForeignKey("authentication.CustomUser", related_name="following", on_delete=models.CASCADE)

    following_user_id = models.ForeignKey("authentication.CustomUser", related_name="followers", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"

