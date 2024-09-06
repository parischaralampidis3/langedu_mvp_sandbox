from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .form import StudentForm, CourseForm, EnrollmentForm, LessonForm, AssignLessonToCourseForm, QuestionContainerForm
from .models import Student, Course, Enrollment, Lesson, QuestionContainer, AssignLessonToCourse

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
    context = {
        "form": form,
        "update": student
    }
    return render(request, './students/update_student.html', context)

def delete_student(request, id):
    delete_entry = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        delete_entry.delete()
        return redirect('students')
    return HttpResponseNotAllowed(['POST'])

def courses(request):
    courses_list = Course.objects.all()
    return render(request, './courses/courses.html', {'courses_list': courses_list})

def course(request, id):
    show_course = get_object_or_404(Course, id=id)
    lesson_enrollments = AssignLessonToCourse.objects.filter(course=show_course)
    context = {
        'course': show_course,
        'lesson_enrollments': lesson_enrollments,
    }
    return render(request, './courses/course.html', context)

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
    return render(request, './courses/create_course.html', context)

def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("courses")
    else:
        form = CourseForm(instance=course)
    context = {
        "form": form,
        "update": course
    }
    return render(request, './courses/update_course.html', context)

def delete_course(request, id):
    delete_entry_course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        delete_entry_course.delete()
        return redirect('courses')
    return HttpResponseNotAllowed(['POST'])

def lessons(request):
    lesson_list = Lesson.objects.all()
    return render(request, 'lessons/lessons.html', {'lesson_list': lesson_list})

def create_lesson(request):
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST)
        if lesson_form.is_valid():
            lesson_form.save()
            return redirect('lessons')  # Redirect to the lessons list page after successful submission
    else:
        lesson_form = LessonForm()  # Initialize an empty form for GET requests

    context = {
        'LessonForm': lesson_form  # Pass the form to the template context
    }
    return render(request, 'lessons/create_lesson.html', context)

def questions(request):
    questions_container = QuestionContainer.objects.all()
    return render(request, './questions/questionsContainer.html', {'questions_list': questions_container})

def create_question_container(request):
    if request.method == 'POST':
        create_question_container_form = QuestionContainer(request.POST)
        if QuestionContainerForm.is_valid():
            create_question_container_form.save()
            return redirect('questions')
    else:
        create_question_container_form = QuestionContainerForm()

    context = {
        'create_question_container_form' : create_question_container_form
    }

    return render(request,'questions/create_question_container', context)


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
    return render(request, './courses/enroll_student.html', context)

def enroll_lesson(request):
    if request.method == 'POST':
        lesson_enrollment_form = AssignLessonToCourseForm(request.POST)
        if lesson_enrollment_form.is_valid():
            lesson_enrollment_form.save()
            return redirect('courses')
    else:
        lesson_enrolment_form = AssignLessonToCourseForm()

    context = {
        'lesson_enrollment_form': lesson_enrolment_form
    }
    return render(request, './courses/enroll_lesson.html', context)




