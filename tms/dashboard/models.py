from django.db import models
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    course_id = models.ForeignKey(Course, on_delete= models.CASCADE)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class Student(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=100)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['email']
    def __str__(self):
        return self.email

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
    is_active = models.BooleanField(default=True)
    difficulty = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='General')  # Set a default value here
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class QuestionContainer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
"""
This class initiates a model that contains model columns for a Text QuestionContainer
"""
class TextQuestionContainer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Allow null values and set on_delete behavior
    question_container = models.ForeignKey(
        QuestionContainer,
        on_delete=models.SET_NULL,
        null=True,  # Allow NULL values in this field
        blank=True  # Optional: Allows this field to be blank in forms
    )
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

"""
This class initiates a model that contains model columns, for a multiple choice container
"""
class MultipleChoiceContainer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default Description')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    question_container = models.ForeignKey(
        QuestionContainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

"""
This class initiates a model that contains model columns, for a text question
"""
class TextQuestion(models.Model):
    question_number_id = models.IntegerField()
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text_question_container = models.ForeignKey(TextQuestionContainer,on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
"""
This class initiates a model that contains model columns for a multiple choice question
"""
class MultipleChoiceQuestion(models.Model):
    multiple_choice_number_id = models.IntegerField()
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    multiple_choice_container = models.ForeignKey(
        MultipleChoiceContainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
"""
This class initiates a model that contains model columns for setting choice attributes for the multiple choice model
"""
class MultipleChoiceOption(models.Model):
    option_number_id = models.IntegerField()
    option = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    multiple_choice_question = models.ForeignKey(MultipleChoiceQuestion,on_delete=models.CASCADE,related_name="multiple_choice_options")
    class Meta:
        unique_together = ('option_number_id', 'multiple_choice_question')
        ordering = ['option']
    def __str__(self):
        return self.option
"""
This class initiates a model that contain model columns for setting answer at corresponding text questions
"""
class Answer(models.Model):
    answer_number_id = models.IntegerField()
    answer_input = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text_question = models.OneToOneField(TextQuestion, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer_input

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_submitted = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class ExerciseQuestion(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
class ExerciseQuestionsAnswer(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    textQuestion = models.ForeignKey(TextQuestion, on_delete=models.CASCADE, related_name='exercise_questions')
    answer = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Question '{self.textQuestion.title}' in {self.exercise.title}"

class ExerciseMutipleQuestionAnswer(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    multipleQuestion = models.ForeignKey(MultipleChoiceQuestion,on_delete=models.CASCADE)
    multipleOptions = models.ForeignKey(MultipleChoiceOption, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question '{self.multipleQuestion.title}' in {self.exercise.title}"

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.title}'

class AssignLessonToCourse(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.lesson.title} assigned to {self.course.title}'

class AssignQuestionContainerToLesson(models.Model):
    question_container = models.ForeignKey(QuestionContainer, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.question_container.title} assigned to {self.lesson.title}'

class AssignMultipleChoiceQuestionContainerToLesson(models.Model):
    multiple_choice_container = models.ForeignKey(MultipleChoiceContainer, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.multiple_choice_container.title} assigned to {self.lesson.title}'


