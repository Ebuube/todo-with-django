from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TodoListCreateAPIView(generics.GenericAPIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response({'message': 'Todo API is wired up'})
