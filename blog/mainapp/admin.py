from django.contrib import admin
from .models import UserBase, Article

# Register your models here.
@admin.register(UserBase)
class AdminUser(admin.ModelAdmin):
    list_display = ('usertag', 'username', 'email', 'date_create')

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_create')