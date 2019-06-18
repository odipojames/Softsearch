from django import forms
from .models import *


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['creater']
