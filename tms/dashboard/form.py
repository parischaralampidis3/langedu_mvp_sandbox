from django import forms
from .models import Student
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, BaseUserManager


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input border pt-5 rounded', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Password'}),
            'dob': forms.DateInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Email'}),
        }
