from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import UserBase
from .forms import RegisterForm, UpdateUserForm, UpdatePasswordForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

# Create your views here.
class RegisterView(CreateView):
    model = UserBase
    form_class = RegisterForm
    success_url = '/login/'


class UserLoginView(LoginView):
    model = UserBase
    template_name = 'mainapp/login.html'


class UserLogoutView(LogoutView):
    model = UserBase


class UserDetail(DetailView):
    model = UserBase
    template_name = 'mainapp/profile.html'


class UserUpdate(UpdateView):
    model = UserBase
    form_class = UpdateUserForm
    template_name = 'mainapp/userbase_update_form.html'
    success_url = '/'


class UserPasswordUpdate(PasswordChangeView):
    model = UserBase
    form_class = UpdatePasswordForm
    template_name = 'mainapp/change_user_password.html'
    success_url = '/'
    