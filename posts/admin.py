from django.contrib import admin
from .models import Post
from .models import Comment


class PostAdmin(admin.ModelAdmin):
    model = Post

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)