from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import datetime


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, name, surname, password=None):
        if not email:
            raise ValueError('Users must have an email address!')

        email = self.normalize_email(email)
        email.lower()
        user = self.model(email=email, username=username, name=name, surname=surname)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, name, surname, password=None):
        user = self.create_user(email, username, name, surname, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'surname']

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_short_name(self):
        return self.name + ' ' + self.surname

    def get_username(self):
        return self.username

    def __str__(self):
        return self.email


class Post(models.Model):
    user = models.ForeignKey(UserAccount, models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    addedDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    addedDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "Komentarz"
