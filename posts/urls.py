from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
# from .views import current_user, UserList

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/all', views.AllPosts.as_view()),
    path('posts/<int:post_id>/', views.post_show),
    path('posts/user/<int:user_id>/', views.user_post_show),
    path('posts/comments/<int:post_id>/', views.PostComments.as_view()),
    path('posts/comments/<int:post_id>/all/', views.comment_post_show),
]

urlpatterns = format_suffix_patterns(urlpatterns)