from django.db.models import Count

from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Услуги', 'url_name': 'products'},
        {'title': 'Формы', 'url_name': 'formspage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},]


forms = [
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'План на месяц', 'url_name': 'page_plan_form'},
    {'title': 'АPI Yandex Direct', 'url_name': 'api_yandex_direct_form'},
    {'title': 'АPI Yandex Metrika', 'url_name': 'api_yandex_metrika_form'},
    {'title': 'АPI Google Analytics', 'url_name': 'api_google_analytics_form'},
    {'title': 'АPI Ozon', 'url_name': 'ozon_api_form'},
    {'title': 'АPI Wildberries', 'url_name': 'api_wildberries_form'},
]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()  #Category.objects.annotate(Count('boards'))  [{'cat_id': 1, 'id__count': 9},]

        user_menu = menu.copy()
        formsList = forms.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        if self.request.user.id != 1:
            formsList.pop(0)


        context['menu'] = user_menu
        context['cats'] = cats
        context['formsList'] = formsList

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
