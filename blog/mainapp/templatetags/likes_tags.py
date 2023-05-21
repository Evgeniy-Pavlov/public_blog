from django import template
from mainapp.models import LikesArticle, Article

register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context):
    likes_user = LikesArticle.objects.filter(article=Article.objects.get(id=context['object'].id), user_liked=context['user'])
    return bool(likes_user)