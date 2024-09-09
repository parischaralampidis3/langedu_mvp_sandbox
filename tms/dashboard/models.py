from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='Default description')
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Student(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
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

class TextQuestion(models.Model):
    title = models.CharField(max_length=255)
    number_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text_question_container = models.ForeignKey(TextQuestionContainer, on_delete=models.CASCADE)

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

