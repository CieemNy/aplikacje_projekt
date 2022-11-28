from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import *
from .permissions import *
from .models import *

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


# endpoint: searching for posts by title
@api_view(['GET'])
def post_title(request, string):
    if request.method == 'GET':
        posts = Post.objects.all().filter(title__icontains=string)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


# endpoint: add comment to post

class CommentAdd(APIView):
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        comment_data = request.data
        new_comment = Comment.objects.create(
            post=post,
            user=request.user,
            content=comment_data['content'],
        )
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)


# endpoint: display comments which are assigned to specific post

class ListCommentsPost(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
