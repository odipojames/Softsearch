from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Task(models.Model):

    name = models.CharField(max_length=50,default="Task")
    creater = models.ForeignKey(User,on_delete=models.CASCADE)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    date = models.DateField(("Date"), default=date.today)
    Done=(

            ('Yes','Yes'),
            ('No','No'),

    )
    Done = models.CharField(max_length=12,choices=Done,default="No")

    def __str__(self):
        return self.name

    def save_task(self):
        self.save()

    def delete_task(self):
        self.delete()

    @classmethod
    def get_task(cls):
        task=Task.objects.all()
        return task
