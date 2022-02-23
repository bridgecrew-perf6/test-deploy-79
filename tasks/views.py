from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import TodoList, Image
from .forms import *




def index(request):
    tasks = TodoList.objects.all()
    form = TodoListForm()
    photo = Image.objects.all()
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks':tasks,
        'form':form,
        'photo':photo,
    }
    return render(request, 'tasks/index.html', context)


def update(request, pk):
    task = TodoList.objects.get(id=pk)
    form = TodoListForm(instance=task)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update.html', context)


def delete(request, pk):

    item = TodoList.objects.get(id=pk)
    if  request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {
        'item':item,
    }
    return render(request, 'tasks/delete.html', context)


def error_404(request, exception):
    return render(request, 'tasks/test.html')