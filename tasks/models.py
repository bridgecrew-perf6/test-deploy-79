from django.db import models


class TodoList(models.Model):
    task_name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

class Image(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=True, blank=False)

    image = models.ImageField(null=False)



   
# Create your models here.
