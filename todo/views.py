# Create your views here.
from django.shortcuts import render
from del3.todo.models import Task

def overview (request):
    
    tasks = Task.objects.all()
    
    return render(request, 'todo/overview.html', {'tasks': tasks})