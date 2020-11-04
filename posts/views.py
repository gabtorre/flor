from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# from posts.serializers import UserSerializerWithToken

from posts.models import Post
from authentication.models import CustomUser
from posts.serializers import PostSerializer
# from posts.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from posts.permissions import IsOwnerOrReadOnly
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        posts = Post.objects.filter(owner=self.request.user.id)
        print(posts)
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_post = Post.objects.create(owner=CustomUser.objects.get(id=self.request.user.id), caption=post_data["caption"], image=post_data["image"])

        new_post.save()

        serializer = PostSerializer(new_post)

        return Response(serializer.data)
        
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class AllPosts(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        posts = Post.objects.all()
        print(posts[0].owner.username)
        return posts

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        
        queryset = Post.objects.get(id=id)
        print(queryset)


@api_view(['GET', 'PUT', 'DELETE'])   
def post_show(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        print(post.owner.id, request.user.id)
        if post.owner.id == request.user.id:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])   
def user_post_show(request, user_id):
    post = Post.objects.filter(owner=user_id)

    if request.method == 'GET':
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)