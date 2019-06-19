from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.


class TaskTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='k')
        self.task = Task.objects.create(id=1,
                                           creater=self.user,
                                           start='13:00',
                                           end='14:00',
                                           date='2019-06-25',
                                           Done='NO')

    def test_instance(self):
        self.assertTrue(isinstance(self.task,Task))


    def test_save_task(self):
        self.task.save()
        task = Task.objects.all()
        self.assertTrue(len(task)>0)

    def test_delete_task(self):
        self.task.delete()
        task = Task.objects.all()
        self.assertTrue(len(task)==0)
