from django import forms
from .models import (
    Student, Course, Enrollment, AssignLessonToCourse, Lesson, QuestionContainer, TextQuestionContainer,
    AssignQuestionContainerToLesson, TextQuestion, ExerciseQuestionsAnswer, Exercise
)

# Form for Student model
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

# Form for Course model
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input border pt-5 rounded', 'placeholder': 'Title'})
        }

# Form for Lesson model
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'is_active']

# Form for QuestionContainer model
class QuestionContainerForm(forms.ModelForm):
    class Meta:
        model = QuestionContainer
        fields = ['title', 'description']

# Form for TextQuestionContainer model
class TextQuestionContainerForm(forms.ModelForm):
    class Meta:
        model = TextQuestionContainer
        fields = ['title', 'description', 'is_active', 'question_container']

# Form for TextQuestion model
class TextQuestionForm(forms.ModelForm):
    class Meta:
        model = TextQuestion
        fields = ['question_number_id', 'title', 'is_active', 'text_question_container']

# Form for ExerciseQuestionsAnswer model
class ExerciseQuestionsAnswerForm(forms.ModelForm):
    class Meta:
        model = ExerciseQuestionsAnswer
        fields = ['exercise', 'textQuestion', 'answer']

# Form for Enrollment model
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

# Form for Exercise model
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['title', 'is_submitted']

# Form for AssignLessonToCourse model
class AssignLessonToCourseForm(forms.ModelForm):
    class Meta:
        model = AssignLessonToCourse
        fields = ['lesson', 'course']

# Form for AssignQuestionContainerToLesson model
class AssignQuestionContainerToLessonForm(forms.ModelForm):
    class Meta:
        model = AssignQuestionContainerToLesson
        fields = ['question_container', 'lesson']

# Form for AssignTextQuestionsToTextQuestionContainer
class AssignTextQuestionsToTextQuestionContainerForm(forms.Form):
    text_question_container = forms.ModelChoiceField(
        queryset=TextQuestionContainer.objects.all(),
        label='Text Question Container'
    )
    text_questions = forms.ModelMultipleChoiceField(
        queryset=TextQuestion.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Text Questions'
    )

# Form for AssignTextQuestionsToExercise
class AssignTextQuestionsToExerciseForm(forms.Form):
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all(),
        label='Exercise'
    )
    text_questions = forms.ModelMultipleChoiceField(
        queryset=TextQuestion.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Text Questions'
    )

    def save(self):
        if not self.is_valid():
            raise ValueError('Form is not valid')

        # Extract cleaned data
        exercise = self.cleaned_data['exercise']
        text_questions = self.cleaned_data['text_questions']

        # Save the relationship
        for question in text_questions:
            ExerciseQuestionsAnswer.objects.create(
                exercise=exercise,
                textQuestion=question,
                answer=None  # Set answer to None or any default value
            )

# Form for answering Exercise Questions
class ExerciseAnswerForm(forms.ModelForm):
    class Meta:
        model = ExerciseQuestionsAnswer
        fields = ['answer']
        widgets = {
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formset for managing multiple answers to Exercise Questions
ExerciseAnswerFormSet = forms.modelformset_factory(
    ExerciseQuestionsAnswer,
    form=ExerciseAnswerForm,
    extra=0
)


