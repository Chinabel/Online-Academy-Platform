from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # ForeignKey to Category
    admin = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_create_course", "Can create a course"),
            ("can_edit_course", "Can edit a course"),
            ("can_delete_course", "Can delete a course"),
        ]

    def __str__(self):
        return self.title

    @property
    def search_vector(self):
        return SearchVector('title', 'description')

class Assignment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    max_marks = models.IntegerField()
    file_upload = models.FileField(upload_to='assignments/%Y/%m/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    class Meta:
        permissions = [
            ("can_create_assignment", "Can create an assignment"),
            ("can_edit_assignment", "Can edit an assignment"),
            ("can_delete_assignment", "Can delete an assignment"),
        ]

    def __str__(self):
        return f"Assignment: {self.title} for {self.course.title}"

class ToDoList(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Assumed User model for student
    task = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"To-Do: {self.task} for {self.user.username}"

class Book(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    publish_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    file_upload = models.FileField(upload_to='books/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.title

class YouTubeVideo(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField()  # URL of the YouTube video
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cms_user_set',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cms_user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.course.title}"