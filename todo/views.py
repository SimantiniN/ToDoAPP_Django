from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404,render
from . import models
from .models import Task

# Create your views here.

def addTask(request):
    data = request.POST['task'] #<input type="text" name="task" class="form-control" placeholder="Add a task here">
    Task.objects.create(task=data) #task is field name  in model Task
    #return HttpResponse("Task addes successfully")#
    return redirect('home')
def mark_as_done(request,pk):
    data = get_object_or_404(Task,pk=pk) #if data not exit return 404
    data.is_completed=True
    # now go to  <a href = {% url mark_as_done%} class="btn btn-success"><i class="fa fa-check"></i> Mark as Done</a>
    data.save()
    return redirect('home')
def mark_as_undone(request,pk):
    data = get_object_or_404(Task,pk=pk) #if data not exit return 404
    data.is_completed=False
    # now go to  <a href = {% url mark_as_done%} class="btn btn-success"><i class="fa fa-check"></i> Mark as Done</a>
    data.save()
    return redirect('home')
def delete(request,pk):
    data = get_object_or_404(Task,pk=pk) #if data not exit return 404
    data.delete()
    return redirect('home')
def edit(request,pk):
    data = get_object_or_404(Task,pk=pk) #if data not exit return 404
    if request.method=='POST':
        edit_data=request.POST['task']
        data.task=edit_data
        data.save()
        return redirect('home')
    else:
        context= {
            'task':data,
        }
        return render(request,'edit_task.html',context)