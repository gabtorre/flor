from django.urls import path 
from .views import AddFollower

urlpatterns = [ 
    path('', AddFollower.as_view(), name="followe_user"),
    ]