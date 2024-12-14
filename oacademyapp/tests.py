from django.test import TestCase
from .models import Assignment, Course, Todo
from django.utils import timezone
from django.urls import reverse, resolve
from .forms import TodoForm
from django.contrib.auth.models import User
from .views import HomeView

# Create your tests here.
class AssignmentModelTest(TestCase):
    def test_create_assignment(self):
        assignment = Assignment.objects.create(
            title="Test Assignment",
            description="This is a test assignment.",
            is_completed=False,
            created_at=timezone.now()
        )
        self.assertEqual(assignment.title, "Test Assignment")
        self.assertEqual(assignment.is_completed, False)

class CourseModelTest(TestCase):
    def test_create_course(self):
        course = Course.objects.create(
            name="Django 101",
            description="An introductory course to Django.",
            duration="3 months",
            start_date=timezone.now()
        )
        self.assertEqual(course.name, "Django 101")
        self.assertEqual(course.duration, "3 months")

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(
            task="Finish Django Project",
            due_date=timezone.now() + timezone.timedelta(days=1),
            is_done=False
        )
        self.assertEqual(todo.task, "Finish Django Project")
        self.assertEqual(todo.is_done, False)

class ViewTest(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of your home URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Online Academy")

    def test_assignment_list_view(self):
        response = self.client.get(reverse('assignments'))  # Replace with the correct URL name for listing assignments
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Assignments")

    def test_course_list_view(self):
        response = self.client.get(reverse('courses'))  # Replace with the correct URL name for listing courses
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Courses")

class FormTest(TestCase):
    def test_todo_form_valid(self):
        form_data = {
            'task': 'Complete Django tutorial',
            'due_date': timezone.now() + timezone.timedelta(days=5),
            'is_done': False
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_todo_form_invalid(self):
        form_data = {
            'task': '',  # Empty task should make the form invalid
            'due_date': timezone.now() + timezone.timedelta(days=5),
            'is_done': False
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('task', form.errors)

class UserRegistrationTest(TestCase):
    def test_registration_view(self):
        url = reverse('register')  # Replace with the correct URL for registration
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")

    def test_user_registration(self):
        url = reverse('register')  # Replace with the correct URL for registration
        data = {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirection after successful registration
        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

class UrlTest(TestCase):
    def test_home_url_resolves_to_home_view(self):
        url = reverse('home')  # Assuming 'home' is the name of your URL for the homepage
        view = resolve(url)
        self.assertEqual(view.func.__name__, HomeView.as_view().__name__)