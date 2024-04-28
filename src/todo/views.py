from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

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


class TodoViewSet(viewsets.ViewSet):
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Todo.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo)

        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoCreateAPIView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoUpdateAPIView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoDestroyAPIView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoAPIView(APIView):
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Todo.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):
    serializer_class = TodoModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo)

        return Response(serializer.data)

    def put(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([permissions.IsAuthenticated])
def todo_list_create(request):
    if request.method == "GET":
        queryset = Todo.objects.all()
        serializer = TodoModelSerializer(queryset, many=True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def todo_detail(request, pk):
    queryset = Todo.objects.all()
    todo = get_object_or_404(queryset, pk=pk)

    if request.method == "GET":
        serializer = TodoModelSerializer(todo)

        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TodoModelSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = TodoModelSerializer(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
