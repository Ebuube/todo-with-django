from django.urls import path
from .views import dashboard, todo_list, todo_create, todo_edit

app_name = 'todos'

urlpatterns = [
  path('', todo_list, name='list'),
  path('dashboard/', dashboard, name='dashboard'),
  path('create/', todo_create, name='create'),
  path('<int:pk>/edit/', todo_edit, name='edit'),
]
