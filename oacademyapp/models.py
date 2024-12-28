# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def get_due_date():
    return timezone.now() + timezone.timedelta(days=7)


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=get_due_date)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    is_completed = models.BooleanField(default=False)
    task = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_assignment(self):
        from .models import Assignment
        return self.assignment

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
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title