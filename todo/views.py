from django.http import HttpResponse
from django.shortcuts import redirect
from . import models
from .models import Task

# Create your views here.

def addTask(request):
    data = request.POST['task'] #<input type="text" name="task" class="form-control" placeholder="Add a task here">
    Task.objects.create(task=data) #task is field name  in model Task
    #return HttpResponse("Task addes successfully")#
    return redirect('home')