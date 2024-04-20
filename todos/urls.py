from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('todos/', todo_list, name='todo-list'),
    path('todos/<int:pk>/', todo_detail, name='todo-detail'),
]
