from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Task
from .forms import Taskform

# Create your views here.
def index(request):
    if request.method=='POST':
        task=request.POST.get('task')
        priority=request.POST.get('priority')
        time=request.POST.get('time')
        tobj=Task(task=task,priority=priority,time=time)
        tobj.save()
        return redirect('/')
    taskall=Task.objects.all()
    return render(request,'index.html',{'task':taskall})

def delete(request,id):
    if request.method=='POST':
        tobj= Task.objects.get(id=id)
        tobj.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    instance=Task.objects.get(id=id)
    tform=Taskform(request.POST or None, instance=instance)
    if tform.is_valid():
        tform.save()
        return redirect('/')
    return render(request,'update.html',{'tform':tform,'instance':instance})

class listview(ListView):
    model=Task
    template_name='index.html'
    context_object_name='task'


class detailview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='tasko'

class updateview(UpdateView):
    model=Task
    template_name='updateview.html'
    context_object_name='tasko'
    fields = ['task','priority','time']

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('listview')