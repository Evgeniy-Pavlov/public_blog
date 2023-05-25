from django import template
from mainapp.models import LikesArticle, Article

register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context):
    """Пользовательский тэг для проверки числа лайков в представлении ArticleDetailView."""
    likes_user = LikesArticle.objects.filter(article=Article.objects.get(id=context['object'].id), user_liked=context['user'])
    return bool(likes_user)


@register.simple_tag(takes_context=True)
def is_liked_in_list(context):
    """Пользовательский тэг для проверки числа лайков в представлении ArticleListView."""
    likes_user = LikesArticle.objects.filter(article=Article.objects.get(id=context['art'].id), user_liked=context['user'])
    return bool(likes_user)
