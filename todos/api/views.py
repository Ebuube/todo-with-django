from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter

from todos.models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    '''
    Security invariants (must match SSR):
    - Authenticated users only
    - Users can only see/manipulate their own todos
    - Owner is always set server-side
    '''
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['created_at', 'due_date', 'updated_at', 'title', 'is_completed']
    ordering = ['-created_at']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
