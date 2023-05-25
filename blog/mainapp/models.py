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
    preview = models.CharField(max_length=500, null=False, default='Это превью статьи к сожалению не было описано.')
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


class LikesArticle(models.Model):
    """Модель хранения лайков к статьям."""
    user_liked = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class News(models.Model):
    """Модель хранения новостей."""
    author = models.ForeignKey(UserBase, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=500, null=False)
    date_create = models.DateTimeField(null=True, default=datetime.now)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'News'


class ImagesNews(models.Model):
    """Модель хранения изображений к новостям."""
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ImagesNews'


class LikesNews(models.Model):
    """Модель хранения лайков к новостям."""
    user_liked = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'LikesNews'

