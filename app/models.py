from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
# class User(models.Model):
#   id = models.UUIDField(default=uuid4)
#   username = models.CharField(max_length=25, unique=true, lowe)
#   name = models.CharField(max_length=200)
#   notes = models.ForeignKey('Note', on_delete=models.CASCADE, default=None,)
#   created_at = models.DateTimeField(auto_add_now=True)
#   modified_at = models.DateTimeField(auto_now=True)

class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  text = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
      return self.title

class Comment(Note):
  