from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import TaskSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        if serializer.validated_data['board'].owner != request.user:
            return Response({'detail': 'You do not own this board'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer.save(owner=request.user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
