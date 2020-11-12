from django.urls import include, path
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('api/', include('authentication.urls')),
    path('follow/', include('followers.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]