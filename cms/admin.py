from django.contrib import admin
from .models import Category, Course, Assignment, Review

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]
    list_display = ('title', 'admin', 'category', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment)
admin.site.register(Review)