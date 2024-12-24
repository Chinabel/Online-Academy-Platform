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
    list_display = ('id', 'title', 'get_assignment_title', 'due_date', 'is_completed')

    def get_assignment_title(self, obj):
        return obj.assignment.title  # Access the 'title' field of the related Assignment model
    get_assignment_title.admin_order_field = 'assignment__title'  # Allow sorting by assignment title
    get_assignment_title.short_description = 'Assignment Title'  # Customize the column header

admin.site.register(Todo, TodoAdmin)
