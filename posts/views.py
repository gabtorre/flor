from django.http import HttpResponse
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import CustomUser
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from posts.permissions import IsOwnerOrReadOnly


""" 
POST VIEWS 
"""

class PostList(APIView):
    """
    List all posts, or create a new post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=CustomUser.objects.get(id=self.request.user.id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        if post.owner.id == request.user.id:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)

        
class UserPosts(APIView):
    """
    Retrieve a user's posts
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
    def get(self, request, pk, format=None):
        posts = Post.objects.filter(owner=pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


""" 
COMMENT VIEWS 
"""

class PostComments(APIView):
    """
    Retrieve comments on a post, and add comment to a post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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