from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

def task_list(request):
    #tasks = Task.objects.all().order_by(
    #    '-priority',      # priorité élevée en premier
    #    'is_completed',   # non complétées avant complétées
    #    'created_at'      # puis par date de création
    #)

    if request.method == 'POST':
        title = request.POST.get('title')
        priority_mapping = {'high': '1', 'medium': '2', 'low': '3'}
        priority = priority_mapping.get(request.POST.get('priority', 'medium'), '2')
        if title:
            Task.objects.create(title=title, priority=priority)
        return redirect('task_list')

    return render(request, 'task_list.html', {'tasks': tasks})
    

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.completed_at = timezone.now() if task.is_completed else None
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')