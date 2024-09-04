from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    #add a description field here
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class CourseMaterial(models.Model):
    course_material_title = models.CharField(max_length=100)
    course_material_description = models.CharField(max_length=100)
    course_material_difficulty = models.CharField(max_length=100)
    course_material_isActive = models.BooleanField(default=True)
    course_material_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['course_material_title']

    def __str__(self):
        return self.course_material_title

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
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.title}'

class AssignCourseToCourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    courseMaterial = models.ForeignKey(CourseMaterial, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.course.title} is assigned in {self.courseMaterial.course_material_title}'