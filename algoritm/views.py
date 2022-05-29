from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Услуги', 'url_name': 'products'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},]



def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'algoritm/index.html', context=context)



class AlgoritmProducts(ListView):
    model = Boards
    template_name = 'algoritm/products.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Услуги'
        context['cat_selected'] = 0

        return context

    def get_queryset(self):
        return Boards.objects.filter(is_published=True)


class AlgoritmCategory(ListView):
    model = Boards
    template_name = 'algoritm/products.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Boards.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'algoritm/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'

        return context


class ShowPost(DetailView):
    model = Boards
    template_name = 'algoritm/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']

        return context


def contact(request):
    return HttpResponse("Страница контакты")

def login(request):
    return HttpResponse("Вход в личный кабинет")

def pageNotFound(request, excexption):
    return HttpResponseNotFound(f"<h1>Такая страница не найдена</h1>")