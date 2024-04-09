from rest_framework import serializers

from .models import Todo


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "due_date", "is_done"]
