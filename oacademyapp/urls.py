from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('courses/', views.course_list, name='courses'),  # List of courses
    path('courses/<int:id>/', views.course_detail, name='course_detail'),  # Course details
    path('assignments/', views.assignments, name='assignments'),  # List of assignments
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),  # Assignment details
    path('todo/', views.todo_list, name='todos'),  # List of todos
    path('todo/<int:id>/', views.todo_detail, name='todo_detail'),  # Todo details
    path('profile/', views.profile, name='profile'),  # User profile
    path('register/', views.register, name='register'),  # User registration
    path('youtube/', views.youtube_video_list, name='youtube'),  # YouTube page
    path('books/', views.book_list, name='books'),  # List of books
    path('about/', views.about, name='about'),
]