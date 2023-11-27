from django.shortcuts import render

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
    return render(            
        request,         
        'tasklist/form.html',
        {}
    )