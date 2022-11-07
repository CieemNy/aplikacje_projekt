from django.urls import path
from django.contrib import admin
from . import views


admin.site.site_url = 'http://127.0.0.1:8000/apk/'
urlpatterns = [
    path('users', views.UserList.as_view(), name='user-list')
]
