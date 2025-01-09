from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from oacademyapp import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
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
    path('set-language/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
