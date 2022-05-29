from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
from .utils import *




def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'algoritm/index.html', context=context)



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
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items()) + list(c_def.items()))

class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'algoritm/addpage.html'
    success_url = reverse_lazy('home')

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

def contact(request):
    return HttpResponse("Страница контакты")

def login(request):
    return HttpResponse("Вход в личный кабинет")

def pageNotFound(request, excexption):
    return HttpResponseNotFound(f"<h1>Такая страница не найдена</h1>")