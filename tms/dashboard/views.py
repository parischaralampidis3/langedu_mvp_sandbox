from django.shortcuts import render, redirect
from .form import StudentForm
from .models import Student

def home(request):
    return render(request, 'index.html')

def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html', {'students_list': students_list})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Redirect to the students list page after successful form submission
    else:
        form = StudentForm()

    return render(request, 'create_student.html', {'form': form})