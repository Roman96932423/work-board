from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import TaskSerializer
from .models import Task
from boards.models import Board


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, board__owner=request.user)
    serializer = TaskSerializer(task)
    
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tasks_create_get(request, board_id):
    board = get_object_or_404(Board, pk=board_id, owner=request.user)
    
    if request.method == 'GET':
        tasks = board.tasks.select_related('owner').all()
        serializer = TaskSerializer(tasks, many=True)
        
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user, board=board)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
