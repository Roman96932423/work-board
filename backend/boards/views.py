from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import BoardSerializer
from .models import Board


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create_board(request):
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
