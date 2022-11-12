from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission

User = get_user_model()


# permission: only owner can edit post/comment

class EditPermissions(BasePermission):
    message = "Only owner of post/comment can editing post/comment"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


# permission: only owner can delete post/comment

class DeletePermissions(BasePermission):
    message = "Only owner of post/comment can delete post/comment"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


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
