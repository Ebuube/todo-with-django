from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def todo_list(request):
    return render(request, 'todos/todo_list.html')
