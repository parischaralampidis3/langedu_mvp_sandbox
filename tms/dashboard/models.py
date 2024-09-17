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

class TextQuestionContainer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
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

class MultipleChoiceQuestionContainer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
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

class TextQuestion(models.Model):
    question_number_id = models.IntegerField()
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text_question_container = models.ForeignKey(TextQuestionContainer,on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title

class MultipleChoiceQuestion(models.Model):
    multiple_choice_number_id = models.IntegerField()
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    answer_number_id = models.IntegerField()
    answer_input = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text_question = models.OneToOneField(TextQuestion, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer_input

class MultipleChoiceAnswer(models.Model):
    multiple_choice_number_id = models.IntegerField()
    multiple_choice_input = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    multiple_choice = models. OneToOneField(MultipleChoiceQuestion, on_delete=models.CASCADE)

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
    textQuestion = models.ForeignKey('TextQuestion', on_delete=models.CASCADE, related_name='exercise_questions')
    answer = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Question '{self.textQuestion.title}' in {self.exercise.title}"

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

