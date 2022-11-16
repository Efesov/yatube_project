from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, pk):
    template = 'posts/group_list.html'
    return render(request, template)
    

# Create your views here.
