from django.urls import path # import from todo_main.urls.py
from todo import views # from . import views
urlpatterns = [
    path('addTask/',views.addTask ,name='addTask'),
    path('mark_as_done/<int:pk>',views.mark_as_done ,name='mark_as_done'),
    path('mark_as_undone/<int:pk>',views.mark_as_undone ,name='mark_as_undone'),
    path('delete/<int:pk>',views.delete ,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
]
# Above is used to call addtask page and Path to show todo url for add
# whchich is from Todo_main import urls - path('todo/',include('todo.urls')),
