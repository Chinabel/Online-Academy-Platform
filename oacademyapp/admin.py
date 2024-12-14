# admin.py
from django.contrib import admin
from .models import Course
from .models import Assignment, Todo

# Customize the admin interface for the Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ['title', 'description']  # Fields to search by in the admin interface
    list_filter = ['created_at']  # Filter by the creation date

admin.site.register(Course, CourseAdmin)

# Admin interface for Assignment model
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at']
    list_filter = ['is_completed']
    ordering = ['created_at']

admin.site.register(Assignment, AssignmentAdmin)

# Admin interface for Todo model
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'assignment', 'due_date', 'is_completed']
    search_fields = ['title', 'description']
    list_filter = ['is_completed', 'due_date']
    ordering = ('due_date',)

admin.site.register(Todo, TodoAdmin)
