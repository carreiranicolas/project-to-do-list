from django.shortcuts import render, redirect
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
