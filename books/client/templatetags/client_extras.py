from django import template
from django.utils.safestring import mark_safe

from app.models import Cart, Category, UserProfile

register = template.Library()


@register.simple_tag
def cart(pk):
    cart, created = Cart.objects.get_or_create(user_id=pk)
    return cart


@register.simple_tag
def categories():
    return Category.objects.filter(parent=None)[:3]


@register.simple_tag
def user_profile(request):
    return UserProfile.objects.get(user=request.user)


