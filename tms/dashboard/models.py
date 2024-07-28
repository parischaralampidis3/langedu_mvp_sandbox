from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomStudentManager(BaseUserManager):
    def create_student(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        student = self.model(email=email, **extra_fields)
        student.set_password(password)
        student.save()
        return student

class Student(AbstractUser):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dob = models.DateField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects = CustomStudentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'lastname']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name


