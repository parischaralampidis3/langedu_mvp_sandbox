from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .form import StudentForm, CourseForm, EnrollmentForm, LessonForm, AssignLessonToCourseForm, QuestionContainerForm, \
    TextQuestionContainerForm,AssignQuestionContainerToLessonForm,TextQuestionForm,AssignTextQuestionsToTextQuestionContainerForm, \
    ExerciseForm,AssignTextQuestionsToExerciseForm
from .form import ExerciseAnswerFormSet
from .models import Student, Course, Enrollment, Lesson, Exercise, QuestionContainer, AssignLessonToCourse,\
    TextQuestionContainer,AssignQuestionContainerToLesson,ExerciseQuestionsAnswer

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

def lesson(request, id):
    show_lesson = get_object_or_404(Lesson, id=id)
    enrollments = AssignQuestionContainerToLesson.objects.filter(lesson=show_lesson)
    context = {
        'lesson': show_lesson,
        'enrollments': enrollments
    }
    return render(request, 'lessons/lesson.html', context)

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

def update_lesson(request,id):
    lesson = get_object_or_404(Lesson, id=id)
    if request.method == 'POST':
        update_lesson_form = LessonForm(request.POST, instance=lesson)
        if update_lesson_form.is_valid():
            update_lesson_form.save()
            return redirect('lessons')
    else:
        update_lesson_form = LessonForm(instance=lesson)
    context = {
        'update_lesson_form': update_lesson_form,
        'update': lesson
    }
    return render(request, './lessons/update_lesson.html', context )

def delete_lesson(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lessons')
    return HttpResponseNotAllowed(['POST'])

def questions(request):
    questions_container = QuestionContainer.objects.all()
    return render(request, './questions/questionsContainer.html', {'questions_container': questions_container})

def create_text_question_container(request):
    if request.method == 'POST':
        create_text_question_container_form = TextQuestionContainerForm(request.POST)
        if create_text_question_container_form.is_valid():
            create_text_question_container_form.save()
            return redirect('questions')  # Redirect to the questions list page after successful form submission
    else:
        create_text_question_container_form = TextQuestionContainerForm()

    # Ensure that we return a response in all cases
    context = {
        'create_text_question_container_form': create_text_question_container_form
    }
    return render(request, 'questions/create_text_question_container.html', context)


def create_question_container(request):
    if request.method == 'POST':
        create_question_container_form = QuestionContainerForm(request.POST)
        if create_question_container_form.is_valid():
            create_question_container_form.save()
            return redirect('questions')
    else:
        create_question_container_form = QuestionContainerForm()

    context = {
        'create_question_container_form': create_question_container_form
    }

    return render(request, 'questions/create_question_container.html', context)


def create_text_question(request):
    if request.method == 'POST':  # Corrected line
        create_text_question_form = TextQuestionForm(request.POST)
        if create_text_question_form.is_valid():
            create_text_question_form.save()
            return redirect('create_text_question')
    else:
        create_text_question_form = TextQuestionForm()
    context = {
        'create_text_question_form': create_text_question_form
    }
    return render(request, 'questions/create_text_question.html', context)


def update_question_container(request, id):
    update = get_object_or_404(QuestionContainer, id=id)
    if request.method == 'POST':
        update_question_container_form = QuestionContainerForm(request.POST, instance=update)
        if update_question_container_form.is_valid():
            update_question_container_form.save()
            return redirect('questions')
    else:
        update_question_container_form = QuestionContainerForm(instance=update)
    context = {
        'update_question_container_form': update_question_container_form,
        'update': update
    }
    return render(request, './questions/update_question_container.html', context)

def delete_question_container(request, id):
    delete_question = get_object_or_404(QuestionContainer, id=id)
    if request.method == 'POST':
        delete_question.delete()
        return redirect('questions')
    return HttpResponseNotAllowed(['POST'])

def exercises(request):
    exercises = Exercise.objects.all()
    return render(request, './exercises/exercises.html', {'exercises': exercises})

def create_exercise_container(request):
    if request.method == 'POST':
        create_exercise_container_form = ExerciseForm(request.POST)
        if create_exercise_container_form.is_valid():
            create_exercise_container_form.save()
            return redirect('exercises')
    else:
        create_exercise_container_form = ExerciseForm()
    context = {
            'create_exercise_container_form': create_exercise_container_form
    }
    return render(request, 'exercises/create_exercise_container.html', context)

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
        lesson_enrollment_form = AssignLessonToCourseForm()

    context = {
        'lesson_enrollment_form': lesson_enrollment_form
    }
    return render(request, './courses/enroll_lesson.html', context)

def enroll_question_to_lesson(request):
    if request.method == 'POST':
        question_to_lesson_enrollment_form = AssignQuestionContainerToLessonForm(request.POST)
        if question_to_lesson_enrollment_form.is_valid():
            question_to_lesson_enrollment_form.save()
            return redirect('lessons')
    else:
        question_to_lesson_enrollment_form = AssignQuestionContainerToLessonForm()

    context = {
        'question_to_lesson_enrollment_form': question_to_lesson_enrollment_form
    }
    return render(request, './lessons/enroll_question_to_lesson.html', context)

def assign_text_questions_to_text_container(request):
    if request.method == "POST":
        text_question_to_container_form = AssignTextQuestionsToTextQuestionContainerForm(request.POST)
        if text_question_to_container_form.is_valid():
            container = text_question_to_container_form.cleaned_data['text_question_container']
            selected_questions = text_question_to_container_form.cleaned_data['text_questions']

            for question in selected_questions:
                question.text_question_container = container
                question.save()

            return redirect('create_text_question')
    else:
        text_question_to_container_form = AssignTextQuestionsToTextQuestionContainerForm()
    context = {
        'text_question_to_container_form': text_question_to_container_form
    }
    return render(request, './questions/assign_text_questions_to_text_container.html', context)

def assign_text_questions_to_exercise_form(request):
    if request.method == "POST":
        assign_form = AssignTextQuestionsToExerciseForm(request.POST)
        if assign_form.is_valid():
            # Use the form's custom save method to handle the saving logic
            assign_form.save()
            return redirect('create_exercise_container')  # Redirect after saving successfully
    else:
        assign_form = AssignTextQuestionsToExerciseForm()  # Initialize the form for GET requests

    # Render the template with the context
    context = {
        'assign_text_questions_to_exercise_form': assign_form
    }
    return render(request, 'exercises/assign_exercise.html', context)



def answer_exercise_question(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    questions = exercise.questions.all()

    if request.method == 'POST':
        formset=ExerciseAnswerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    answer_instance = form.save(commit=False)
                    answer_instance.user = request.user
                    answer_instance.save()
            return redirect('exercises')
        else:
            formset = ExerciseAnswerFormSet(queryset=ExerciseQuestionsAnswer.objects.none())
        context = {
            'exercise': exercise,
            'questions': questions,
            'formset': formset
        }

        return render(request, 'exercises/answer_exercise.html', context)
