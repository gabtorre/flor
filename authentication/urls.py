from django.urls import path 
from rest_framework_simplejwt import views as jwt_views 
from .views import ObtainTokenPairWithColorView, CustomUserCreate, UserAPI, UserList, user_show

from authentication import views

urlpatterns = [ 
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'), 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/current_user/', UserAPI.as_view(), name='current_user'),
    path('users/', UserList.as_view()),
    path('users/<int:user_id>/', views.user_show),
    ]