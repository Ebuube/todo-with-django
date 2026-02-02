from django.urls import path
from . import api_views


urlpatterns = [
  path('todos/', api_views.TodoListCreateAPIView.as_view(), name='api_todo_list_create'),
]
