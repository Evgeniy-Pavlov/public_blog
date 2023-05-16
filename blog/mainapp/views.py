from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import UserBase, Article
from .forms import RegisterForm, UpdateUserForm, UpdatePasswordForm, ArticleForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

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


class ArticleCreate(CreateView):
    """Представление создания статьи."""
    model = Article
    form_class = ArticleForm
    template_name = 'mainapp/article_form.html'
    success_url = '/'


class ArticleUpdate(UpdateView):
    """Представление редактирования и обновления статьи."""
    model = Article
    form_class = ArticleForm
    template_name = 'mainapp/article_form.html'
    success_url = '/'
    