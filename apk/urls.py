from django.urls import path
from django.contrib import admin
from . import views


admin.site.site_url = 'http://127.0.0.1:8000/apk/'
urlpatterns = [
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('posts', views.PostList.as_view(), name='forum-post-list'),
    path('posts/add', views.CreatePost.as_view(), name='forum-post-create'),
    path('posts/edit/<int:pk>', views.PostEdit.as_view(), name='forum-post-edit'),
    path('posts/delete/<int:pk>', views.PostDelete.as_view(), name='forum-post-delete'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='forum-post-detail'),
]
