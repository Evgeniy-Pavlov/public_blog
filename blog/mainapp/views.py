from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, FormView
from .models import UserBase, Article, LikesArticle, News, ImagesNews
from .forms import RegisterForm, UpdateUserForm, UpdatePasswordForm, ArticleForm, ArticleDeleteForm, CommentsArticleCreateForm, LikesArticleAddForm, NewsForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
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
    success_url = '/'


class UserLogoutView(LogoutView):
    """Класс реализации логаута."""
    model = UserBase


class UserDetail(LoginRequiredMixin, DetailView):
    """Представление профиля пользователя."""
    model = UserBase
    login_url = '/login/'

    def get(self, request, pk):
        if not UserBase.objects.get(username=self.request.user).is_company:
            template_name = 'mainapp/profile.html'
            return render(template_name=template_name, request=request)
        else:
            template_name = 'mainapp/company-profile.html'
            return render(template_name=template_name, request=request)


class UserUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Представление обновления профиля пользователя."""
    model = UserBase
    login_url = '/login/'
    form_class = UpdateUserForm
    template_name = 'mainapp/userbase_update_form.html'
    success_message = 'Изменения в профиле сохранены'

    def get_success_url(self):
        return f'/profile/{self.request.user.id}'



class UserPasswordUpdate(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    """Представление формы обновления пароля."""
    model = UserBase
    login_url = '/login/'
    form_class = UpdatePasswordForm
    template_name = 'mainapp/change_user_password.html'
    success_message = 'Пароль был успешно изменен'
    
    def get_success_url(self):
        return f'/profile/{self.request.user.id}'


class ArticleList(ListView):
    """Представление статей списком."""
    model = Article
    template_name = 'mainapp/article_list.html'


class ArticleDetail(DetailView):
    """Представление статьи для чтения."""
    model = Article
    template_name = 'mainapp/article_detail.html'


class ArticleCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Представление создания статьи."""
    login_url = '/login/'
    model = Article
    form_class = ArticleForm
    template_name = 'mainapp/article_form.html'
    success_url = '/'
    success_message = 'Статья успешно опубликована.'

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ArticleUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Представление редактирования и обновления статьи."""
    login_url = '/login/'
    model = Article
    form_class = ArticleForm
    template_name = 'mainapp/article_form.html'
    success_url = '/'
    success_message = 'Изменения в статье сохранены'

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
        

class CreateNews(LoginRequiredMixin, FormView):
    """Представление для создания новостей."""
    login_url = '/login/'
    success_url = '/'
    template_name = 'mainapp/news_create.html'
    form_class = NewsForm

    def form_valid(self, form: NewsForm) :
        news_data = News.objects.create(author = self.request.user, text = form.cleaned_data['text'])
        images = form.cleaned_data['images']
        if images:
            for image in images:
                ImagesNews.objects.create(news = news_data, image = image)
        return super().form_valid(form)





