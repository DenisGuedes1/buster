from users.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from movies.permission import AuthUser
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserId(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated, AuthUser]
   
    def get(self, request: Request, user_id=int):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        return Response(UserSerializer(user).data)
    
    def patch(self, request: Request, user_id=int):
        user = get_object_or_404(User, id=user_id)
        print('user', user)
        self.check_object_permissions(request, user)
        print('data', request.data)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
