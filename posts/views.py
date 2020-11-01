from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.serializers import UserSerializerWithToken

from posts.models import Post
from authentication.models import CustomUser
from posts.serializers import PostSerializer
from posts.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from posts.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user.id)
        # return self.request.user.posts.all()

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_post = Post.objects.create(owner=CustomUser.objects.get(id=self.request.user.id), caption=post_data["caption"], image=post_data["image"])

        new_post.save()

        serializer = PostSerializer(new_post)

        return Response(serializer.data)
        
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        queryset = Post.objects.filter(owner=self.request.user.id)
    
    

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)