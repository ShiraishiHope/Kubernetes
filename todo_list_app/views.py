from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, created_at=timezone.now())
        return redirect('task_list')
    return render(request, 'task_list.html', {'tasks': tasks})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')