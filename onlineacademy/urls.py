from codecs import register
import profile
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from oacademyapp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contact'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('oacademyapp.urls')),
    path('courses/', views.courses, name='courses'),
    path('courses/', include('oacademyapp.urls')),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('assignments/', views.assignments, name='assignments'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('todo/', views.todo, name='todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('profile/', views.profile, name='profile'),
    path('youtube/', views.youtube_video_list, name='youtube'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)