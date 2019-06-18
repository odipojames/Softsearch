from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import *
from . forms import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TaskSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    current_user = request.user
    task = Task.objects.filter(creater=current_user)
    return render(request,'home.html', {"date":date,"task":task})

def do_today(request):
    current_date = dt.date.today()
    item = Task.objects.filter(date=current_date)
    return render(request,'today.html',{"item":item})


@login_required(login_url='/accounts/login/')
def new_task(request):
    current_user = request.user
    if request.method =='POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creater = current_user
            task.save()
            messages.success(request,'new task created successfuly')
        return redirect('home')
    else:
        form = NewTaskForm()
        return render(request,'new_task.html',{"form":form})


def updateTask(request,pk):

    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        form =NewTaskForm(request.POST,instance=task)

        try:
          if form.is_valid():
            task=form.save(commit=False)
            task.save()
            messages.success(request,'Task has been updated successfuly')
            return redirect(home)
        except Exception as e:

            HttpResponse(request, 'your records are not saved')
    else :
        form = NewTaskForm(instance=task)

        return render(request, 'updateTask.html', {'form':form,"task":task})


def deleteTask(request, id):

    task = Task.objects.get(pk=id)
    task.delete()
    messages.warning(request,'task deleted')
    return redirect(home)
    return render(request, 'updateTask.html', {'task': task})


def confirm_delete(request,id):

    task = Task.objects.get(pk=id)
    return render(request,'delete.html',{'task':task})




class TaskApi(APIView):
    def get(self, request, format=None):
        all_task = Task.objects.all()
        serializers = TaskSerializer(all_task, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = TaskSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
