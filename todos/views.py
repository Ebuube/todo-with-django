from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
            messages.success(request, 'Todo created.')
            return redirect('todos:list')
    else:
        form = TodoForm()

    return render(request, 'todos/todo_form.html', {'form': form, 'page_title': 'Create todo'})

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated.')
            return redirect('todos:list')
    else:
        form = TodoForm(instance=todo)

    return render(
        request,
        'todos/todo_form.html',
        {'form': form, 'todo': todo, 'page_title': 'Edit todo'},
    )

@login_required
def dashboard(request):
    qs = Todo.objects.filter(owner=request.user)

    total_count = qs.count()
    completed = qs.filter(is_completed=True).count()
    pending = qs.filter(is_completed=False).count()

    recent = qs.order_by('-id')[:5]

    context = {
        'total': total_count,
        'completed': completed,
        'pending': pending,
        'recent': recent,
    }
    return render(request, 'todos/dashboard.html', context)

@login_required
def todo_list(request):
    qs = Todo.objects.filter(owner=request.user)

    status = request.GET.get('status', 'all')
    q = (request.GET.get('q') or '').strip()

    if status == 'pending':
        qs = qs.filter(is_completed=False)
    elif status == 'completed':
        qs = qs.filter(is_completed=True)

    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))

    todos = qs.order_by('is_completed', 'created_at')

    context = {
        'todos': todos,
        'status': status,
        'q': q,
    }
    return render(request, 'todos/todo_list.html', context)
