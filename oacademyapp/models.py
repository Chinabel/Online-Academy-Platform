# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Course(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=255, default='Default Assignment')
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assignment = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    task = models.TextField(blank=True)  # Assuming 'task' refers to a description of the todo
    status = models.BooleanField(default=False)  # Assuming 'status' refers to completion status
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Dictionary(models.Model):
    word = models.CharField(max_length=255)
    definition = models.TextField()

    def __str__(self):
        return self.word


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"Profile of {self.user.username}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title