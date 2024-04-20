from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the TodoItem model.

    This serializer serializes TodoItem objects, including the associated user's username.

    Attributes:
        username: A read-only field that includes the username of the user associated with the TodoItem.
    """
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'completed', 'created_at','username']
