from django.contrib import admin
from .models import UserAccount, Post


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'name', 'surname']


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'addedDate']


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Post, PostAdmin)

