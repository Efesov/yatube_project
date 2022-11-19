from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

def index(request):
    template = 'posts/index.html'
    OneG = 'Это главная страница проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'OneG': OneG,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'info': 'info',}
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    info = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'info': info,
    }
    return render(request, template, context)