from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
from .views import current_user, UserList

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('current_user/', current_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)