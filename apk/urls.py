from django.urls import path
from django.contrib import admin
from . import views
from .views import CommentAdd, ListCommentsPost

admin.site.site_url = 'http://127.0.0.1:8000/apk/'
urlpatterns = [
    # user endpoints
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    # posts endpoints
    path('posts', views.PostList.as_view(), name='forum-post-list'),
    path('posts/add', views.CreatePost.as_view(), name='forum-post-create'),
    path('posts/edit/<int:pk>', views.PostEdit.as_view(), name='forum-post-edit'),
    path('posts/delete/<int:pk>', views.PostDelete.as_view(), name='forum-post-delete'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='forum-post-detail'),
    path('posts/<str:string>', views.post_title, name='search-post-title'),
    # comments endpoints
    path('posts/<int:pk>/comments/add', CommentAdd.as_view(), name='comment-post-add'),
    path('posts/<int:pk>/comments', ListCommentsPost.as_view(), name='comments-post-display'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment-detail'),
    path('comment/edit/<int:pk>', views.CommentEdit.as_view(), name='comment-edit'),
    path('comment/delete/<int:pk>', views.CommentDelete.as_view(), name='comment-delete'),
    path('comments/<int:pk>', views.user_comments, name='search-user-comments')
]
