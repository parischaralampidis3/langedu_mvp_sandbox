
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers  import StudentSerializer
from .form import StudentForm
from .models import Student

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def home(request):
    return render(request, 'index.html')

def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html', {'students_list': students_list})

def student(request, id):
    show_student = Student.objects.get(id=id)
    context = {
        'student': show_student,
    }
    return render(request, 'student.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Redirect to the students list page after successful form submission
    else:
        form = StudentForm()

    return render(request, 'create_student.html', {'form': form})



def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    context = {"form": form, "update": student}
    return render(request, 'update_student.html', context)


def delete_student(request, id):
    delete_entry = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        delete_entry.delete()
        return redirect('students')
    return HttpResponseNotAllowed(['POST'])
