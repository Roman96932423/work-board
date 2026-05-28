from django.db.models import (
    CharField, 
    TextField, 
    ForeignKey, 
    DateTimeField, 
    CASCADE,
    Model)
from django.contrib.auth.models import User


class Board(Model):
    title = CharField(max_length=50)
    description = TextField(blank=True)
    owner = ForeignKey(User, on_delete=CASCADE, related_name='boards')
    created_at = DateTimeField(auto_now_add=True)
