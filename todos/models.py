from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    """
    Model representing a todo item.

    Attributes:
        user (User): The user who created the todo item.
        title (str): The title of the todo item.
        completed (bool): Indicates whether the todo item is completed or not.
        created_at (datetime): The date and time when the todo item was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
