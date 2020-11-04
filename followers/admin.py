from django.contrib import admin
from .models import UserFollowing

# Register your models here.


class FollowAdmin(admin.ModelAdmin):
    model = UserFollowing

admin.site.register(UserFollowing, FollowAdmin)