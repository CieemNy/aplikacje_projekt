from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from .permissions import *

User = get_user_model()


# endpoint: display list of users

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-list'


# endpoint: display, edit, delete user details

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-details'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


# endpoint: display list of posts

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-list'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: create post

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-create'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: edit single post

class PostEdit(generics.UpdateAPIView, EditPermissions):
    permission_classes = [EditPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-edit'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: delete single post

class PostDelete(generics.DestroyAPIView, DeletePermissions):
    permission_classes = [DeletePermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-delete'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: display single post

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'forum-post-detail'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
