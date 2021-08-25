from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 120) # Field for title of todo-item
    description = models.TextField() # Text field for description of todo-item
    completed = models.BooleanField(default = False) # Status of completion for the todo-item, defaulting to false

    def _str_(self):
        return self.title