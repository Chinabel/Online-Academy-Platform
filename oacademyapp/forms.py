from django import forms
from dataclasses import fields
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['title','description']


class DateInput(forms.DateInput):
    input_type='date'

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        widgets={'due':DateInput()}
        fields = ['title']

class DashboardForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Search', 'required': 'true'}),
    max_length=50, label='', required=False)

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'task', 'status']  

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'email']
