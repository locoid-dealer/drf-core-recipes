from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    due_date = models.DateField()
    is_done = models.BooleanField()
