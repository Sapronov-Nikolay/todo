from .models import Task
from django.shortcuts import render
import rocket  # Это название вашего проекта

def get_menu(active):
    result = []
    for elem in rocket.urls.navset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result

def index(request):
    context = {
         'navset': get_menu('/'),
    }
    return render(
        request,
        'mainpage/index.html',
        context)

def index(request):
    result = ""
    for t in Task.objects.all():
        result += t.description
    kateg = ""    
    #for a in Kategorii.objects.all():
    #    kateg += a.kategoriya    
    return render(
        request,
        "mainpage/index.html",
        {"Задачи": Task.objects.all(), "Категории": kateg} # Kонтекст передаваемых переменных

    )