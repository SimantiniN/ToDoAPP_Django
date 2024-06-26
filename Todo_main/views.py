#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    #return HttpResponse('<h1>This is HomePage</h1>')
    tasks=Task.objects.filter(is_completed=False).order_by('-created_at') # - sign show in dscending order
    completed_tasks =Task.objects.filter(is_completed=True).order_by('modified_at') 
    
    # print(tasks)
    context = {
                'tasks':tasks,
                'completed_tasks':completed_tasks
              }
    return render(request,'home.html',context) # set templates folder in settings.py
