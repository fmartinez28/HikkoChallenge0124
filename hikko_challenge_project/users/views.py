from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from .service import UserService

@api_view(['GET'])
def get_users_followers(request):
    try:
        users = UserService.get_users_and_followers()
        return Response(users, status=status.HTTP_200_OK)
    except:
        return Response(status=400)
@api_view(['GET'])
def get_least_followers_user(request):
    try:
        user = UserService.get_least_followers_user()
        return Response(user)
    except:
        return Response(status=400)