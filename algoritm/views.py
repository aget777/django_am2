from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
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

def products(request):
    posts = Boards.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Услуги',
        'cat_selected' : 0,
    }
    return render(request, 'algoritm/products.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Boards.objects.filter(cat_id=cat[0].id)


    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat[0].id,
    }
    return render(request, 'algoritm/products.html', context=context)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Boards.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'algoritm/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def show_post(request, post_slug):
    post = get_object_or_404(Boards, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post_slug
    }
    return render(request, 'algoritm/post.html', context=context)


def contact(request):
    return HttpResponse("Страница контакты")

def login(request):
    return HttpResponse("Вход в личный кабинет")

def pageNotFound(request, excexption):
    return HttpResponseNotFound(f"<h1>Такая страница не найдена</h1>")