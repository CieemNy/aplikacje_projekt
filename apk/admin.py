from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'name', 'surname']


admin.site.register(UserAccount, UserAccountAdmin)
