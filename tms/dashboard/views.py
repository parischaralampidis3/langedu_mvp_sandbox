from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
from .form import StudentForm  # Ensure the correct import name

def home(request):
    return render(request, 'index.html')

def students(request):
    return render(request, 'users.html')

def index_students(request):
    users_list = Student.objects.all()
    return render(request, 'users.html', {'users_list': users_list})

def show_student(request, slug):
    try:
        user = Student.objects.get(slug=slug)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'user_detail.html', {'user': user})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_users')
    else:
        form = StudentForm()
    return render(request, 'create_user.html', {'form': form})