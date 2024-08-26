
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed


from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers  import StudentSerializer
from .form import StudentForm
from .models import Student

from .form import StudentForm,CourseForm
from .models import Student, Course

from .form import StudentForm, CourseForm, EnrollmentForm
from .models import Student, Course, Enrollment


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
    return render(request, './students/students.html', {'students_list': students_list})

def student(request, id):
    show_student = get_object_or_404(Student, id=id)
    enrollments = Enrollment.objects.filter(student=show_student)
    context = {
        'student': show_student,
        'enrollments': enrollments,
    }
    return render(request, './students/student.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Redirect to the students list page after successful form submission
    else:
        form = StudentForm()

    return render(request, './students/create_student.html', {'form': form})

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
    return render(request, './students/update_student.html', context)


def delete_student(request, id):
    delete_entry = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        delete_entry.delete()
        return redirect('students')
    return HttpResponseNotAllowed(['POST'])

def courses(request):
    courses_list = Course.objects.all()
    return render(request, 'courses.html', {'courses_list': courses_list})

def course(request, id):
    show_course = Course.objects.get(id=id)
    context = {
        'course.html': show_course
    }
    return render(request, 'course.html', context)

def create_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('courses')  # Redirect to the courses list page after successful form submission
    else:
        course_form = CourseForm()

    context = {
        'CourseForm': course_form  # Pass the form as 'CourseForm' to match the template
    }
    return render(request, './create_course.html', context)

def enroll_student(request):
    if request.method == 'POST':
        enrollment_form = EnrollmentForm(request.POST)
        if enrollment_form.is_valid():
            enrollment_form.save()
            return redirect('courses')  # Redirect to a success page or another relevant page
    else:
        enrollment_form = EnrollmentForm()  # Initialize an empty form for GET requests

    context = {
        'enrollment_form': enrollment_form  # The key should match the form variable name in the template
    }
    return render(request, 'enroll_student.html', context)




