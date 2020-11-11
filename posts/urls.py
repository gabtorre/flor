from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/user/<int:pk>/', views.UserPosts.as_view()),
    path('posts/comments/<int:pk>/', views.PostComments.as_view()),
    path('posts/comments/<int:pk>/all/', views.PostComments.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)