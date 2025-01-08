from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from oacademyapp import views
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
from oacademyapp.views import login_view, logout_view
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('admin/', admin.site.urls),
    path('cms/', include('cms.urls')),
    path('courses/', views.courses, name='courses'),  # List of courses
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),  # Course details
    path('assignments/', views.assignments, name='assignments'),  # List of assignments
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),  # Assignment details
    path('todo/', views.todo, name='todo'),  # Todo list
    path('add_todo/', views.add_todo, name='add_todo'),  # Add todo
    path('profile/', views.profile, name='profile'),  # Profile page
    path('profile/complete/', views.profile_completion, name='profile_completion'),
    path('youtube/', views.youtube_video_list, name='youtube'),  # YouTube page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),
    path('logout', views.logout_view, name='logout_no_slash'),
    path('logged-out/', views.logged_out, name='logged_out'),
    path('register/', views.register, name='register'),  # Register page
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Password reset
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('books/', views.books, name='books'),  # List of books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Book details
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('set_language/', set_language, name='set_language'),
    path('accounts/', include('allauth.urls')),
]+ i18n_patterns(
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
