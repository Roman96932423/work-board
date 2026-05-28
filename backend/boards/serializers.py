from rest_framework.serializers import ModelSerializer

from .models import Board


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'description', 'owner', 'created_at']
        
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
            'created_at': {'read_only': True}
        }
