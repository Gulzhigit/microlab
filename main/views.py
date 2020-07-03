from django.shortcuts import render, redirect
from .models import Micro
from .forms import MicroForm


def index(request):
    micros = Micro.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'micros': micros})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = MicroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
            
    form = MicroForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
    
