from django.urls import include, path
# from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('token-auth/', obtain_jwt_token)
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]