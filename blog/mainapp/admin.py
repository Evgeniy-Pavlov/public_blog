from django.contrib import admin
from .models import UserBase, Article
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
    list_display = ('title', 'author', 'date_create')
    form = ArticleAdminForm