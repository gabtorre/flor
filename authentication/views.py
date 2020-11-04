from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework import status, permissions, generics
from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer 

from authentication.models import CustomUser

from rest_framework.decorators import api_view

from django.http import HttpResponse, JsonResponse


class ObtainTokenPairWithColorView(TokenObtainPairView): 
    serializer_class = MyTokenObtainPairSerializer 
    

class CustomUserCreate(APIView): 
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CustomUserSerializer

    def get_object(self):
        # user = CustomUser.objects.get(id=self.request.user.id)
        # print(self.request.user_id)
        # return CustomUser.objects.get(id=self.request.user.id)
        return self.request.user

class UserList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view(['GET', 'PUT', 'DELETE'])   
def user_show(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print(request.data)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        
        # user.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)

        print(user.id, request.user.id)
        if user.id == request.user.id:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)