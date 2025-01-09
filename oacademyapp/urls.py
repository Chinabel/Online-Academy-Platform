from django.conf import settings
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import logout_view, login_view
from . import views

app_name = 'oacademyapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('cms/', include('cms.urls')),
    path('courses/', views.courses, name='courses'),
    path('assignments/', views.assignments, name='assignments'),
    path('todo/', views.todo, name='todo'),
    path('profile/', views.profile, name='profile'),
    path('youtube/', views.youtube_video_list, name='youtube'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
]