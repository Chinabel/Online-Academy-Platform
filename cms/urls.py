from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('search/', views.search_courses, name='search_courses'),
]
