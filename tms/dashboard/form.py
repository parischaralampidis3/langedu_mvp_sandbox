from django import forms
from .models import Student, Course, Enrollment, AssignLessonToCourse, Lesson, QuestionContainer,AssignQuestionContainerToLesson


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

class QuestionContainerForm(forms.ModelForm):
    class Meta:
        model = QuestionContainer
        fields = ['title','description']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

class AssignLessonToCourseForm(forms.ModelForm):
    class Meta:
        model = AssignLessonToCourse
        fields = ['lesson', 'course']

class AssignQuestionContainerToLessonForm(forms.ModelForm):
    class Meta:
        model = AssignQuestionContainerToLesson
        fields = ['question_container', 'lesson']

