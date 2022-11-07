from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions


User = get_user_model()


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    query = User.objects.all()
    serializer = UserCreateSerializer
    name = 'user-list'

