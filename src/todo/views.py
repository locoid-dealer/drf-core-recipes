from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from .models import Todo
from .serializers import TodoModelSerializer

# Create your views here.


class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoGenericViewSet(
    viewsets.GenericViewSet,
    generics.mixins.ListModelMixin,
    generics.mixins.CreateModelMixin,
    generics.mixins.RetrieveModelMixin,
    generics.mixins.UpdateModelMixin,
    generics.mixins.DestroyModelMixin,
):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]
