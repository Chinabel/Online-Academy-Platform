from django.conf import settings
from django.conf.urls import include, url
from django.urls import include, path
from .views import logout_view, login_view
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
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
    path('profile/complete/', views.profile_completion, name='profile_completion'),
    path('register/', views.register, name='register'),  # User registration
    path('login/', login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),
    path('logout', views.logout_view, name='logout_no_slash'),
    path('logged-out/', views.logged_out, name='logged_out'),
    path('youtube/', views.youtube_video_list, name='youtube'),  # YouTube page
    path('books/', views.book_list, name='books'),  # List of books
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('set_language/', set_language, name='set_language'),
    path('accounts/', include('allauth.urls')),
]+ i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', views.home, name='home'),
    path('cms/', include('cms.urls')),
    path('courses/', views.courses, name='courses'),
    path('assignments/', views.assignments, name='assignments'),
    path('todo/', views.todo, name='todo'),
    path('profile/', views.profile, name='profile'),
    path('youtube/', views.youtube_video_list, name='youtube'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
)
