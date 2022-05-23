from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = ['Главная', 'Услуги', 'О нас']


def index(request):

    return render(request, 'algoritm/index.html', {'menu': menu, 'title' : 'Главная страница'})

def products(request):
    posts = Boards.objects.all()
    return render(request, 'algoritm/products.html', {'posts': posts, 'menu': menu, 'title' : 'О сайте'})



