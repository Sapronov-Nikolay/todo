from django.shortcuts import render
from .forms import TaskForm
from mainpage.models import Task

def index(request): 
    return render(     # returns HttpResponse
        request,       # Запрос в точност, как мы его получили
        "tasklist/index.html",
        {
           # будет другое ваапче 'var': param
        } # Kонтекст передаваемых переменных

    )

def add_task(request):
    if request.method == 'POST':
        print(request.POST)
        task_data = TaskForm(request.POST)
        if task_data.is_valid():
            print(task_data.cleaned_data)
        t = Task(**task_data.cleaned_data)
        t.save()
    task_form = TaskForm()
    return render(            
        request,         
        'tasklist/form.html',
        {
            'task_form_auto_gen': task_form
        }
    )