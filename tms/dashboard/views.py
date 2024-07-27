from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')

def index_users(request):
    users_list = User.objects.all()
    return render(request, 'templates/users.html', {'users_list': users_list})

def show_user(request):