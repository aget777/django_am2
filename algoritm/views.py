from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView, FormView

from .models import *
from .forms import *
from .utils import *



class AlgoritmHome(DataMixin, TemplateView):

    template_name = 'algoritm/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')

        return dict(list(context.items()) + list(c_def.items()))


class AlgoritmProducts(DataMixin, ListView):
    model = Boards
    template_name = 'algoritm/products.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Услуги')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Boards.objects.filter(is_published=True)


class AlgoritmCategory(DataMixin, ListView):
    model = Boards
    template_name = 'algoritm/products.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Boards.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        # c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'algoritm/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')

        return dict(list(context.items()) + list(c_def.items()))

class ShowPost(DataMixin, DetailView):
    model = Boards
    template_name = 'algoritm/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))

# def contact(request):
#     return HttpResponse("Страница контакты")
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'algoritm/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def pageNotFound(request, excexption):
    return HttpResponseNotFound(f"<h1>Такая страница не найдена</h1>")

class RegisterUsers(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'algoritm/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'algoritm/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


class FormsPage(DataMixin, ListView):

    template_name = 'algoritm/formspage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Выбор формы')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Boards.objects.filter(is_published=True)

class AddPlan(LoginRequiredMixin, DataMixin, CreateView):
    form_class = PlanForm
    template_name = 'algoritm/page_plan_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление Плана на месяц')

        return dict(list(context.items()) + list(c_def.items()))

class AddYandexDirectApiKey(LoginRequiredMixin, DataMixin, CreateView):
    form_class = YandexDirectForm
    template_name = 'algoritm/api_yandex_direct_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление АПИ ключа Яндекс Директ')

        return dict(list(context.items()) + list(c_def.items()))


class AddYandexMetrikaApiKey(LoginRequiredMixin, DataMixin, CreateView):
    form_class = YandexMetrikaForm
    template_name = 'algoritm/api_yandex_metrika_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление АПИ ключа Яндекс Метрика')

        return dict(list(context.items()) + list(c_def.items()))

class AddGoogleAnalyticsApiKey(LoginRequiredMixin, DataMixin, CreateView):
    form_class = GoogleAnalyticsForm
    template_name = 'algoritm/api_google_analytics_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление АПИ ключа Google Analytics')

        return dict(list(context.items()) + list(c_def.items()))

class AddOzonApiKey(LoginRequiredMixin, DataMixin, CreateView):
    form_class = OzonForm
    template_name = 'algoritm/ozon_api_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление АПИ ключа Ozon')

        return dict(list(context.items()) + list(c_def.items()))

class AddWildberriesApiKey(LoginRequiredMixin, DataMixin, CreateView):
    form_class = WildberriesForm
    template_name = 'algoritm/api_wildberries_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление АПИ ключа Wildberries')

        return dict(list(context.items()) + list(c_def.items()))