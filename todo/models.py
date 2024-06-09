from django.db import models

# Create your models here.Register your models in admin.py
class Task(models.Model):
    task= models.CharField(max_length=300)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.task #It reflect the task name in the admin side.

