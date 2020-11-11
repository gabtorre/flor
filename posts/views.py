from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse, Http404

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from posts.permissions import IsOwnerOrReadOnly


""" 
POST VIEWS 
"""

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        posts = Post.objects.filter(owner=self.request.user.id)
        print(posts)
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        print(request.data)

        new_post = Post.objects.create(owner=CustomUser.objects.get(id=self.request.user.id), caption=post_data["caption"], soundcloud=post_data["soundcloud"], beatport=post_data["beatport"], bandcamp=post_data["bandcamp"], image=post_data["image"])

        new_post.save()

        serializer = PostSerializer(new_post)

        return Response(serializer.data)


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


""" 
COMMENT VIEWS 
"""

class PostComments(APIView):
    """
    Retrieve comments on a post, and add comment to a post.
    """
    def get(self, request, pk, format=None):
        comment = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post = Post.objects.get(id=pk), user = CustomUser.objects.get(id=self.request.user.id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)