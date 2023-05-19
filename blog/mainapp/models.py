from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class UserBase(AbstractUser):
    """Модель для хранения профилей пользователей."""
    usertag = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    last_name = models.CharField(null=True, max_length=20)
    first_name = models.CharField(null=True, max_length=20)
    patronymic = models.CharField(null=True, max_length=20)
    date_create = models.DateTimeField(default=datetime.now)
    is_company = models.BooleanField(default=False)
    company = models.CharField(blank=True, null=True, max_length=20, unique=True)
    about_me = models.CharField(null=True, max_length=500)
    logo = models.ImageField(upload_to='userbase', blank=True, null=True)


class Article(models.Model):
    """Модель для хранения статей."""
    title = models.CharField(max_length=60, null=False)
    body = models.TextField(null=False)
    date_create = models.DateTimeField(null=True, default=datetime.now)
    author = models.ForeignKey(UserBase, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)


class CommentsArticle(models.Model):
    """Модель хранения комментариев к статьям"""
    commentator = models.ForeignKey(UserBase, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text_comments = models.CharField(max_length=400)
    date_create = models.DateTimeField(default=datetime.now)

