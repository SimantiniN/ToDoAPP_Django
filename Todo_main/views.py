#from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse('<h1>This is HomePage</h1>')
    return render(request,'home.html') # set templates folder in settings.py