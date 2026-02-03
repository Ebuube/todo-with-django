from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Todo


@login_required
def todo_list(request):
    todos = (
        Todo.objects
        .filter(owner=request.user)
        .order_by('is_completed', '-created_at')
    )
    return render(request, 'todos/todo_list.html', {'todos': todos})
