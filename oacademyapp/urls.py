from django.urls import include, path
from . import views

app_name = 'oacademyapp'

urlpatterns = [
    path('home/', views.home, name='home'),  # Home view (optional if needed separately)
    path('courses/', views.course_list, name='courses'),  # List of courses
    path('courses/<int:id>/', views.course_detail, name='course_detail'),  # Course details
    path('assignments/', views.assignments, name='assignments'),  # List of assignments
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),  # Assignment details
    path('todo/', views.todo_list, name='todos'),  # Todo list
    path('todo/<int:id>/', views.todo_detail, name='todo_detail'),  # Todo details
    path('profile/', views.profile, name='profile'),  # User profile
    path('register/', views.register, name='register'),  # User registration
    path('youtube/', views.youtube_video_list, name='youtube'),  # YouTube page
    path('books/', views.book_list, name='books'),  # List of books
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('set_language/<str:lang_code>/', views.set_language, name='set_language'),
    path('accounts/', include('allauth.urls')),
]
