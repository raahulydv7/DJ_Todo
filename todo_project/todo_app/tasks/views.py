from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def task_list(request):
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'active':
        tasks = Task.objects.exclude(status='completed')
    elif status_filter == 'completed':
        tasks = Task.objects.filter(status='completed')
    else:  # 'all' or any other value
        tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
        'status_filter': status_filter,
    }
    return render(request, 'tasks/index.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'completed'
    task.save()
    messages.success(request, 'Task marked as completed!')
    return redirect('task_list')