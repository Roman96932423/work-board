from django.contrib.auth.models import User
from django.db.models import (
    Model, 
    CharField, 
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    TextChoices
)

from boards.models import Board


class Task(Model):
    class Status(TextChoices):
        TODO = 'todo', 'To Do'
        IN_PROGRESS = 'in_progress', 'In progress'
        DONE = 'done', 'Done'
        
    class Priority(TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
    
    title = CharField(max_length=70)
    description = TextField(blank=True)
    status = CharField(max_length=11, choices=Status.choices, default=Status.TODO)
    priority = CharField(max_length=6, choices=Priority.choices, default=Priority.MEDIUM)
    board = ForeignKey(Board, on_delete=CASCADE, related_name='tasks')
    owner = ForeignKey(User, on_delete=CASCADE, related_name='tasks')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
