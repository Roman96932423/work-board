from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .serializers import WorkspaceSerializer
from .models import Workspace


@extend_schema(
    request=WorkspaceSerializer,
    responses=WorkspaceSerializer
)
@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def workspace_detail_update(request, ws_id):
    if request.method == 'GET':
        workspace = get_object_or_404(Workspace, pk=ws_id, members=request.user)
        serializer = WorkspaceSerializer(workspace)
        
        return Response(serializer.data)
    
    workspace = get_object_or_404(Workspace, pk=ws_id, owner=request.user)
    
    if request.method == 'PATCH':
        serializer = WorkspaceSerializer(instance=workspace, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
@extend_schema(
    request=WorkspaceSerializer,
    responses=WorkspaceSerializer
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def workspace_list_create(request):
    if request.method == 'GET':
        workspaces = request.user.workspaces.all()
        serializer = WorkspaceSerializer(workspaces, many=True)
        
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = WorkspaceSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
