from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import UserBase, Article
from django import forms


class RegisterForm(UserCreationForm):
    """Форма регистрации."""

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    usertag = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Тэг пользователя')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Адрес электронной почты')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Подтверждение пароля')

    class Meta:
        model = UserBase
        fields = ('username', 'usertag', 'email', 'password1', 'password2', 'is_company', 'company', 'logo')


class UpdateUserForm(forms.ModelForm):
    """Форма обновления пользователя."""

    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    usertag = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Тэг пользователя')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Адрес электронной почты')
    about_me = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Обо мне')

    class Meta:
        model = UserBase
        fields = ('username', 'usertag', 'email', 'about_me', 'is_company', 'company', 'logo')


class UpdatePasswordForm(PasswordChangeForm):
    """Форма обновления пароля пользователя."""

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Старый пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Подтвердите новый пароль')

    class Meta:
        model = UserBase
        fields = ('old_password', 'password1', 'password2')


class ArticleForm(forms.ModelForm):
    """Форма создания статьи пользователем."""

    title = forms.CharField(label='Заголовок')
    body = forms.CharField(widget=CKEditorUploadingWidget(), label='Тело статьи')
    

    class Meta:
        model = Article
        fields = ('title', 'body')
    
