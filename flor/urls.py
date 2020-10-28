from django.urls import include, path
# from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls'))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]