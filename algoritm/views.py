from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Страница приложения')

def categories(request, catid):
    return HttpResponse(f'<h1>Страница категории</h1><p>{catid}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Такая страница не найдена</h1>')