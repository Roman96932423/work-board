from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'board', 'owner', 'created_at', 'updated_at']
        
        read_only_fields = ['board', 'owner', 'created_at', 'updated_at']
