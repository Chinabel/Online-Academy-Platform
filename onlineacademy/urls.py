from codecs import register
import profile
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from oacademyapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.oacademyapp, name='oacademyapp'),
    path('admin/', admin.site.urls),
    path('', include('oacademyapp.urls')),
    path('courses/', views.courses, name='courses'),
    path('courses/', include('oacademyapp.urls')),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('assignments/', views.assignments, name='assignments'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('todo/', views.todo, name='todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('profile/', views.profile, name='profile'),
    path('youtube/', views.youtube, name='youtube'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]