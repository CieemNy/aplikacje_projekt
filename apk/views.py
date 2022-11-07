from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions


User = get_user_model()


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-list'

