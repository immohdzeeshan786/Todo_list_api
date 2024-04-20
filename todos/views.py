from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem
from .serializers import TodoItemSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    """
    View function to list all todo items or create a new todo item.

    GET request:
        Returns a list of all todo items associated with the authenticated user.

    POST request:
        Creates a new todo item for the authenticated user.

    Returns:
        Response: List of todo items or newly created todo item with appropriate status code.
    """
    if request.method == 'GET':
        todos = TodoItem.objects.filter(user=request.user)
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo_detail(request, pk):
    """
    View function to retrieve, update, or delete a todo item.

    GET request:
        Retrieves the details of the specified todo item.

    PUT request:
        Updates the specified todo item.

    DELETE request:
        Deletes the specified todo item.

    Returns:
        Response: Todo item details or success status with appropriate status code.
    """

    try:
        todo = TodoItem.objects.get(pk=pk, user=request.user)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoItemSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoItemSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response({'msg':"deleted successfully"},status=status.HTTP_204_NO_CONTENT)
