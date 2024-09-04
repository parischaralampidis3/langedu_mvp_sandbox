from django import forms
from .models import Student, Course, Enrollment, CourseMaterial, AssignCourseToCourseMaterial, Lesson


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input border pt-5 rounded', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Username'}),
            'dob': forms.DateInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Date of Birth',
                                          'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-input border rounded', 'placeholder': 'Email'}),
        }
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # add a description string at fields array
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input border pt-5 rounded', 'placeholder': 'Title'})
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'is_active']

class CourseMaterialForm(forms.ModelForm):

    class Meta:
        model = CourseMaterial
        fields = ['course_material_title', 'course_material_description', 'course_material_isActive',
                  "course_material_difficulty", "course_material_category"]

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

class AssignCourseToCourseMaterialForm(forms.ModelForm):

    class Meta:
        model = AssignCourseToCourseMaterial
        fields = ['course', 'courseMaterial']