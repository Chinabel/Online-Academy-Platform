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
        fields = ['title', 'description', 'task', 'due_date', 'is_completed', 'status']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now():
            raise forms.ValidationError("Due date cannot be in the past!")
        return due_date  

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > 500:
            raise forms.ValidationError("Bio cannot be longer than 500 characters.")
        return bio
