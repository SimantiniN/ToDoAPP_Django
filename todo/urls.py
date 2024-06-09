from django.urls import path # import from todo_main.urls.py
from todo import views # from . import views
urlpatterns = [
    path('addTask/',views.addTask ,name='addTask'),
    # Above is used to call addtask page and Path to show todo url for add
    # whchich is from Todo_main import urls - path('todo/',include('todo.urls')),
]