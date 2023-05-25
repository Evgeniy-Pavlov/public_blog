from django.contrib import admin
from .models import UserBase, Article, CommentsArticle, LikesArticle, News, ImagesNews, LikesNews, CommentsNews
from ckeditor.widgets import CKEditorWidget
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'


# Register your models here.
@admin.register(UserBase)
class AdminUser(admin.ModelAdmin):
    list_display = ('usertag', 'username', 'email', 'date_create')
    

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_create', 'deleted')
    form = ArticleAdminForm


@admin.register(CommentsArticle)
class AdminCommentsArticle(admin.ModelAdmin):
    list_display = ('commentator', 'article', 'text_comments', 'date_create')


@admin.register(LikesArticle)
class AdminLikesArticle(admin.ModelAdmin):
    list_display = ('user_liked', 'article')


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('author', 'text', 'date_create', 'deleted')


@admin.register(ImagesNews)
class AdminImageNews(admin.ModelAdmin):
    list_display = ('news', 'image')


@admin.register(LikesNews)
class AdminLikesArticle(admin.ModelAdmin):
    list_display = ('user_liked', 'news')


@admin.register(CommentsNews)
class AdminCommentsArticle(admin.ModelAdmin):
    list_display = ('commentator', 'news', 'text_comments', 'date_create')