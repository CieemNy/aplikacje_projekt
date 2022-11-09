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


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-details'

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-list'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-create'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
