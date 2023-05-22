from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import UserBase, Article, CommentsArticle, LikesArticle
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
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    patronymic = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Отчество')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Адрес электронной почты')
    about_me = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Обо мне')
    is_company = forms.BooleanField(label='Признак корпоративного аккаунта.', required=False)
    company = forms.CharField(max_length=20, label='Название компании')
    logo = forms.ImageField(label='Фото профиля', widget=forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}))

    class Meta:
        model = UserBase
        fields = ('username', 'usertag', 'last_name', 'first_name', 'patronymic', 'email', 'about_me', 'is_company', 'company', 'logo')


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

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 850px;'}), label='Заголовок')
    preview = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 850px;'}), label='Превью статьи')
    body = forms.CharField(widget=CKEditorUploadingWidget(), label='Тело статьи')
    

    class Meta:
        model = Article
        fields = ('title', 'preview', 'body')


class ArticleDeleteForm(forms.ModelForm):
    """Форма удаления статьи"""

    class Meta:
        model=Article
        fields = ()


class CommentsArticleCreateForm(forms.ModelForm):
    """Форма создания комментария."""

    class Meta:
        model = CommentsArticle
        fields = ('text_comments',)


class LikesArticleAddForm(forms.ModelForm):
    """Форма добавления лайков к статьям."""

    class Meta:
        model = LikesArticle
        fields = ()

