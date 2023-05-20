from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
from .models import UserBase, Article, LikesArticle
from .forms import RegisterForm, UpdateUserForm, UpdatePasswordForm, ArticleForm, ArticleDeleteForm, CommentsArticleCreateForm, LikesArticleAddForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RegisterView(CreateView):
    """Представление формы регистрации."""
    model = UserBase
    form_class = RegisterForm
    success_url = '/login/'


class UserLoginView(LoginView):
    """Представление формы авторизации."""
    model = UserBase
    template_name = 'mainapp/login.html'


class UserLogoutView(LogoutView):
    """Класс реализации логаута."""
    model = UserBase


class UserDetail(DetailView):
    """Представление профиля пользователя."""
    model = UserBase
    template_name = 'mainapp/profile.html'


class UserUpdate(UpdateView):
    """Представление обновления профиля пользователя."""
    model = UserBase
    form_class = UpdateUserForm
    template_name = 'mainapp/userbase_update_form.html'
    success_url = '/'


class UserPasswordUpdate(PasswordChangeView):
    """Представление формы обновления пароля."""
    model = UserBase
    form_class = UpdatePasswordForm
    template_name = 'mainapp/change_user_password.html'
    success_url = '/'


class ArticleList(ListView):
    """Представление статей списком."""
    model = Article
    template_name = 'mainapp/article_list.html'


class ArticleDetail(DetailView):
    """Представление статьи для чтения."""
    model = Article
    template_name = 'mainapp/article_detail.html'


class ArticleCreate(LoginRequiredMixin, CreateView):
    """Представление создания статьи."""
    login_url = '/login/'
    model = Article
    form_class = ArticleForm
    template_name = 'mainapp/article_form.html'
    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    """Представление редактирования и обновления статьи."""
    login_url = '/login/'
    model = Article
    form_class = ArticleForm
    template_name = 'mainapp/article_form.html'
    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class ArticleDelete(LoginRequiredMixin, UpdateView):
    """Представление удаления статьи.
    Статье проставляется признак удаления и она более в общем списке не отображается."""
    login_url = '/login/'
    model = Article
    form_class = ArticleDeleteForm
    template_name = 'mainapp/delete_article.html'
    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        form.instance.deleted = True
        return super().form_valid(form)
    

class CommentsCreate(LoginRequiredMixin, View):
    """Класс создания комментариев"""
    login_url = '/login/'

    def post(self, request, pk):
        if request.POST['text_comments']:
            form = CommentsArticleCreateForm(request.POST)
            form.instance.commentator = self.request.user
            form.instance.article = Article.objects.get(id=pk)
            form.save()
            return redirect(f'/article-detail/{pk}')
        else:
            return redirect(f'/article-detail/{pk}')


class LikesArticleAdd(LoginRequiredMixin, View):
    """Представление для добавления лайков пользователями к статьям."""
    login_url = '/login/'

    def post(self, request, pk):
        if not LikesArticle.objects.filter(article=Article.objects.get(id=pk), user_liked=self.request.user):
            form = LikesArticleAddForm(request.POST)
            form.instance.user_liked = self.request.user
            form.instance.article = Article.objects.get(id=pk)
            form.save()
            return redirect(f'/article-detail/{pk}')
        else:
            LikesArticle.objects.filter(article=Article.objects.get(id=pk), user_liked=self.request.user).delete()
            return redirect(f'/article-detail/{pk}')
        

