from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, FormView
from .models import UserBase, Article, LikesArticle, News, ImagesNews, LikesNews
from .forms import RegisterForm, UpdateUserForm, UpdatePasswordForm, ArticleForm,\
    ArticleDeleteForm, CommentsArticleCreateForm, LikesArticleAddForm, NewsForm, \
    NewsDeleteForm, LikesNewsAddForm, CommentsNewsCreateForm
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


class UserDetailView(LoginRequiredMixin, DetailView):
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


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Представление обновления профиля пользователя."""
    model = UserBase
    login_url = '/login/'
    form_class = UpdateUserForm
    template_name = 'mainapp/userbase_update_form.html'
    success_message = 'Изменения в профиле сохранены'

    def get_success_url(self):
        return f'/profile/{self.request.user.id}'



class UserPasswordUpdateView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    """Представление формы обновления пароля."""
    model = UserBase
    login_url = '/login/'
    form_class = UpdatePasswordForm
    template_name = 'mainapp/change_user_password.html'
    success_message = 'Пароль был успешно изменен'
    
    def get_success_url(self):
        return f'/profile/{self.request.user.id}'


class ArticleListView(ListView):
    """Представление статей списком."""
    model = Article
    template_name = 'mainapp/article_list.html'


class ArticleDetailView(DetailView):
    """Представление статьи для чтения."""
    model = Article
    template_name = 'mainapp/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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
    

class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
    
    
class ArticleDeleteView(LoginRequiredMixin, UpdateView):
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
    
    

class CommentsCreateView(LoginRequiredMixin, View):
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


class LikesArticleAddView(LoginRequiredMixin, View):
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
        

class LikesArticleListAddView(LoginRequiredMixin, View):
    """Представление для добавления лайков пользователями к статьям в ленте статей."""
    login_url = '/login/'

    def post(self, request, pk):
        if not LikesArticle.objects.filter(article=Article.objects.get(id=pk), user_liked=self.request.user):
            form = LikesArticleAddForm(request.POST)
            form.instance.user_liked = self.request.user
            form.instance.article = Article.objects.get(id=pk)
            form.save()
            return redirect('/')
        else:
            LikesArticle.objects.filter(article=Article.objects.get(id=pk), user_liked=self.request.user).delete()
            return redirect('/')
        

class CreateNewsView(LoginRequiredMixin, FormView):
    """Представление для создания новостей."""
    login_url = '/login/'
    success_url = '/news-list/'
    template_name = 'mainapp/news_create.html'
    form_class = NewsForm

    def form_valid(self, form: NewsForm) :
        news_data = News.objects.create(author = self.request.user, text = form.cleaned_data['text'])
        images = form.cleaned_data['images']
        if images:
            for image in images:
                ImagesNews.objects.create(news = news_data, image = image)
        return super().form_valid(form)


class NewsListView(ListView):
    """Представление ленты новостей."""
    model = News
    template_name = 'mainapp/news_list.html'


class NewsDeleteView(LoginRequiredMixin, UpdateView):
    """Представление удаления новости.
    Новости проставляется признак удаления и она более в общем списке не отображается."""
    login_url = '/login/'
    model = News
    form_class = NewsDeleteForm
    template_name = 'mainapp/delete_news.html'
    success_url = '/news-list/'

    def form_valid(self, form) -> HttpResponse:
        form.instance.deleted = True
        return super().form_valid(form)


class LikesNewsAddListView(LoginRequiredMixin, View):
    """Представление для добавления лайков пользователями к статьям."""
    login_url = '/login/'

    def post(self, request, pk):
        if not LikesNews.objects.filter(news=News.objects.get(id=pk), user_liked=self.request.user):
            form = LikesNewsAddForm(request.POST)
            form.instance.user_liked = self.request.user
            form.instance.news = News.objects.get(id=pk)
            form.save()
            return redirect('/news-list/')
        else:
            LikesNews.objects.filter(news=News.objects.get(id=pk), user_liked=self.request.user).delete()
            return redirect('/news-list/')
        

class NewsDetailView(DetailView):
    """Представление для подробного просмотра новости и ее комментирования."""
    model = News
    template_name = 'mainapp/news_detail.html'


class CommentsNewsCreateView(LoginRequiredMixin, View):
    """Класс создания комментариев к новостям.""" 
    login_url = '/login/'

    def post(self, request, pk):
        if request.POST['text_comments']:
            form = CommentsNewsCreateForm(request.POST)
            form.instance.commentator = self.request.user
            form.instance.news = News.objects.get(id=pk)
            form.save()
            return redirect(f'/news-detail/{pk}')
        else:
            return redirect(f'/news-detail/{pk}')
        

class SearchArticleView(ListView):
    """Представление поиска для статей."""
    template_name = 'mainapp/search.html'

    def get_queryset(self):
        search_request = self.request.GET.get('search')
        return Article.objects.filter(Q(title__icontains= search_request) | Q(preview__icontains=search_request) | Q(body__icontains=search_request) & Q(deleted=False))
    
    def get_context_data(self, *, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        print(context)
        return context