from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Course, Assignment, Todo, Dictionary, Profile, Book
from .forms import *
from django.contrib import messages
from django.views import generic
from django.urls import reverse
from youtubesearchpython import VideosSearch
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def oacademyapp(request):
    # Your view logic here
    return render(request, 'template_name.html', {})

def home(request):
    """
    Home page view.
    """
    courses = Course.objects.all()
    assignments = Assignment.objects.all()

    return render(request, 'home.html', {'courses': courses, 'assignments': assignments})

def index(request):
    items = items.object.order_by("-publish_date")
    now = datetime.datetime.now()
    return render(request,'portfolio/index.html', {"items": items, "year": now.year})

def courses(request):
    """
    View to list all available courses.
    """
    course_list = Course.objects.all()
    return render(request, 'courses.html', {'courses': course_list})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    """
    View to display the details of a specific course.
    """
    try:
        course = Course.objects.get(id=course_id)  # Retrieve course by ID
    except Course.DoesNotExist:
        return HttpResponse("Course not found", status=404)  # Handle course not found

    return render(request, 'course_detail.html', {'course': course})


def assignments(request):
    """
    View to list all assignments.
    """
    assignment_list = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': assignment_list})


def assignment_detail(request, assignment_id):
    """
    View to show details of a specific assignment.
    """
    try:
        assignment = Assignment.objects.get(id=assignment_id)  # Get assignment by ID
    except Assignment.DoesNotExist:
        return HttpResponse("Assignment not found", status=404)

    return render(request, 'assignment_detail.html', {'assignment': assignment})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'oacademyapp/assignment_list.html', {'assignments': assignments})

def youtube(request):
    """
    View to display YouTube content or videos (can be based on user or popular videos).
    """
    # Here, API can be used to fetch YouTube data
    youtube_videos = [
        {"title": "Learn Django", "url": "https://www.youtube.com/watch?v=xxxxxx"},
        {"title": "Django for Beginners", "url": "https://www.youtube.com/watch?v=yyyyyy"},
    ]
    return render(request, 'youtube.html', {'videos': youtube_videos})


def todos(request):
    """
    View to manage and display to-do items.
    """
    todos_list = Todo.objects.filter(user=request.user)  # Filter todos for logged-in user
    return render(request, 'todos.html', {'todos': todos_list})

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo_detail.html', {'todo': todo})

def add_todo(request):
    """
    View to add a new to-do item.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        new_todo = Todo(title=title, user=request.user)
        new_todo.save()
        return redirect('todos')  # Redirect to the todos list page

    return render(request, 'add_todo.html')


def books(request):
    """
    View to list all books available in the academy.
    """
    book_list = Book.objects.all()  # Assuming a 'Book' model
    return render(request, 'books.html', {'books': book_list})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'oacademyapp/book_list.html', {'books': books})

def book_detail(request, book_id):
    """
    View to display the details of a specific book.
    """
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

    return render(request, 'book_detail.html', {'book': book})


def dictionary(request):
    """
    View to display the dictionary (could be a glossary of terms).
    """
    words = Dictionary.objects.all()  # Assuming a 'Dictionary' model with terms
    return render(request, 'dictionary.html', {'words': words})


def register(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    View to handle user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return HttpResponse("Invalid credentials", status=401)

    return render(request, 'login.html')


def logout_view(request):
    """
    View to handle user logout.
    """
    logout(request)
    return redirect('home')


def profile(request):
    """
    View to display and update user profile.
    """
    if request.method == 'POST':
        user_profile = request.user.profile
        user_profile.bio = request.POST.get('bio', user_profile.bio)  # Update bio
        user_profile.save()

    return render(request, 'profile.html', {'profile': request.user.profile})