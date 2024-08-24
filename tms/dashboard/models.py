from django.db import models
<<<<<<< HEAD
=======

>>>>>>> course
class Course(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
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
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default = True)
    username = models.CharField(max_length=100)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email


