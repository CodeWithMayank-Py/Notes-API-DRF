from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model. This serializer converts Note model instances
    to JSON format and vice versa. It includes the fields 'id', 'title', 'content',
    and 'created_at'.
    """
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at']
