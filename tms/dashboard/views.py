from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from .form import UserForm  # Ensure the correct import name

def home(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')

def index_users(request):
    users_list = User.objects.all()
    return render(request, 'users.html', {'users_list': users_list})

def show_user(request, slug):
    try:
        user = User.objects.get(slug=slug)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'user_detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_users')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})