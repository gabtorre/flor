from django.urls import path 
from .views import CustomUserCreate, CurrentUser, UserDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication import views

urlpatterns = [ 
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('user/current_user/', CurrentUser.as_view(), name='current_user'),
    path('users/<int:pk>/', UserDetail.as_view())
    ]