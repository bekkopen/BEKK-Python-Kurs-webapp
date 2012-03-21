# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from del3.todo.models import Task
from del3.todo.forms import TaskForm

def overview (request):
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Task saved! \o/')
        else:
            messages.error(request, 'Something was wrong in the form :(')
    
    else:
        form = TaskForm()
            
    tasks = Task.objects.all()    
    
    return render(request, 'todo/overview.html', {'tasks': tasks, 'form': form})
