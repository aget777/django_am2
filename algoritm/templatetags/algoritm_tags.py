from django import template
from algoritm.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('algoritm/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    cats = Category.objects.all()

    return {'cats': cats, 'cat_selected': cat_selected}