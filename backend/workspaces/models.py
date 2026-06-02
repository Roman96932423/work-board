from django.db.models import (
    CharField, 
    TextField, 
    ForeignKey, 
    ManyToManyField,
    DateTimeField, 
    CASCADE,
    Model)
from django.contrib.auth.models import User


class Workspace(Model):
    name = CharField(max_length=50)
    description = TextField(blank=True)
    owner = ForeignKey(User, related_name='owned_workspaces', on_delete=CASCADE)
    members = ManyToManyField(User, related_name='workspaces', blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
