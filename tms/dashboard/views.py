from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
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


def delete_student(request, id):
    delete_entry = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        delete_entry.delete()
        return redirect('students')
    return HttpResponseNotAllowed(['POST'])
