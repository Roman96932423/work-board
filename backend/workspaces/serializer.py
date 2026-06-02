from rest_framework.serializers import ModelSerializer

from .models import Workspace


class WorkspaceSerializer(ModelSerializer):
    def create(self, validated_data):
        workspace = Workspace.objects.create(**validated_data)
        workspace.members.add(workspace.owner)
            
        return workspace
			
    
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'owner', 'members', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'members', 'created_at', 'updated_at']
