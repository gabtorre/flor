from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from .models import UserFollowing
from authentication.models import CustomUser

# Create your views here.
# class AddFollower(APIView):
#     permission_classes = [
#         permissions.AllowAny,
#     ]
#     def post(self, request, format=None):
#         user = CustomUser.objects.get(user_id=self.request.data.get('id'))
#         UserFollowing.objects.create(user_id=user.id, following_user_id=follow.id)

class AddFollower(APIView):
    
    def post(self, requset, format=None):
        user = CustomUser.objects.get(user_id=self.request.data.get('user_id'))
        follow = CustomUser.objects.get(user_id=self.request.data.get('follow'))

        UserFollowing.objects.create(user_id=user.id, following_user_id=follow.id)
        print(str(user) + ", " + str(follow))
        return JsonResponse({'status':status.HTTP_200_OK, 'data':"", 'message':"follow"+str(follow.user_id)})
