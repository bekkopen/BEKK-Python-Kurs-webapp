from django import forms
from del3.todo.models import Task

class TaskForm (forms.ModelForm):    
    class Meta:
        model = Task