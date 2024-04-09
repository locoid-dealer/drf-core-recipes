from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Todo
from .serializers import TodoModelSerializer

# Create your views here.


class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]
