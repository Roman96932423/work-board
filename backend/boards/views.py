from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import BoardSerializer
from .models import Board


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def board_detail_update_delete(request, board_id):
    if request.method == 'GET':
        board = get_object_or_404(Board, pk=board_id, owner=request.user)
        serializer = BoardSerializer(board)
        
        return Response(serializer.data)
    
    if request.method == 'PATCH':
        board = get_object_or_404(Board, pk=board_id, owner=request.user)
        serializer = BoardSerializer(instance=board, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        board = get_object_or_404(Board, pk=board_id, owner=request.user)
        board.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def boards_list_create(request):
    if request.method == 'GET':
        boards = Board.objects.filter(owner=request.user).select_related('owner')
        serializer = BoardSerializer(boards, many=True)
    
        return Response(serializer.data)
    
    if request.method == 'POST':
    
        serializer = BoardSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
