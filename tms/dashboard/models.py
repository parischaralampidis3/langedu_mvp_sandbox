from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)


