from rest_framework import serializers
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
    owner_id = serializers.CharField(source='owner.id', read_only=True)
    owner_avatar = serializers.CharField(source='owner.avatar', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'image', 'caption', 'owner', 'owner_avatar', 'owner_id', 'timestamp', 'soundcloud', 'beatport', 'bandcamp']


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user', read_only=True)
    id = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['comment', 'username', 'id']