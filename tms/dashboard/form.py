from django import forms
from .models import Student, Course, Enrollment


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input border pt-5 rounded', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Username'}),
            'dob': forms.DateInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Email'}),
        }
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input border pt-5 rounded', 'placeholder': 'Title'})
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
