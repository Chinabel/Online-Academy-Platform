"""
URL configuration for onlineacademy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from codecs import register
import profile
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from oacademyapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.oacademyapp, name='oacademyapp'),
    path('admin/', admin.site.urls),
    path('', include('oacademyapp.urls')),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('assignments/', views.assignments, name='assignments'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('todos/', views.todos, name='todos'),
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