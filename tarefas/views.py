from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .forms import TarefasForm

# Create your views here.

def home(request):
    tasks = Tarefas.objects.all()
    total_tasks = len(tasks)
    completed_tasks = 0
    remaining_tasks = 0
    pct = 0

    for task in tasks:
        if task.feita == True:
            completed_tasks += 1


    remaining_tasks = total_tasks - completed_tasks


    if total_tasks >= 1:
        pct = (completed_tasks/total_tasks) * 100



    return render(
        request, 
        'tarefas/home.html',
        {
            'tasks': tasks,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'remaining_tasks': remaining_tasks,
            'pct': pct

        })

def add(request):
    form = TarefasForm(request.POST)
    
    if form.is_valid():
        form.save()
    return redirect('home')


def toggle(request, id):

    task = get_object_or_404(Tarefas, id=id)

    if task.feita == True:
        task.feita = False
    else:
        task.feita = True
    
    task.save()
    
    return redirect('home')

def delete(request, id):
    task = get_object_or_404(Tarefas, id=id)
    task.delete()
    return redirect('home')
