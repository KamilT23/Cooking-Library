from django import template
from main.models import *
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def add_fav_rec(title):
    return user.profile.favorite_recipes.add(recipe.objects.get(title_recipe=title))

@register.simple_tag
def rem_fav_rec(title):
    return user.profile.favorite_recipes.remove(recipe.objects.get(title_recipe=title))
