"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp.views import RegisterView, UserLoginView, UserLogoutView, UserUpdateView, UserDetailView, \
UserPasswordUpdateView, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, \
ArticleDeleteView, CommentsCreateView, LikesArticleAddView, CreateNewsView, NewsListView, LikesArticleListAddView, \
NewsDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('user-update/<int:pk>', UserUpdateView.as_view()),
    path('profile/<int:pk>', UserDetailView.as_view()),
    path('change-password/<int:pk>', UserPasswordUpdateView.as_view()),
    path('', ArticleListView.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('article-detail/<int:pk>', ArticleDetailView.as_view()),
    path('article-create/', ArticleCreateView.as_view()),
    path('article-update/<int:pk>', ArticleUpdateView.as_view()),
    path('article-delete/<int:pk>', ArticleDeleteView.as_view()),
    path('comments-create/<int:pk>', CommentsCreateView.as_view()),
    path('liked/<int:pk>', LikesArticleAddView.as_view()),
    path('news-create/', CreateNewsView.as_view()),
    path('news-list/', NewsListView.as_view()),
    path('liked-in-list/<int:pk>', LikesArticleListAddView.as_view()),
    path('news-delete/<int:pk>', NewsDeleteView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
