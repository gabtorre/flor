from rest_framework import serializers
from .models import UserFollowing 

class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = '__all__'

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = '__all__'