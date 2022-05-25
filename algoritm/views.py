from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

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
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'posts': posts,
        'menu': menu,
        'title': 'Услуги',
        'cat_selected' : 0,
    }
    return render(request, 'algoritm/products.html', context=context)


def show_category(request, cat_id):
    posts = Boards.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }
    return render(request, 'algoritm/products.html', context=context)


def addpage(request):
    return HttpResponse("Добавить статью")

def show_post(request, post_id):
    return HttpResponse(f"{post_id}")


def contact(request):
    return HttpResponse("Страница контакты")

def login(request):
    return HttpResponse("Вход в личный кабинет")

def pageNotFound(request, excexption):
    return HttpResponseNotFound(f"<h1>Такая страница не найдена</h1>")