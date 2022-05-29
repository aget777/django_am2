from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Услуги', 'url_name': 'products'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
