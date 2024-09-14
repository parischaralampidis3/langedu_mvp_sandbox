
from django.urls import path


from .views import home, students, student, create_student, update_student, enroll_student, delete_student, courses, \
    course, create_course, update_course, delete_course, lessons, lesson, create_lesson, update_lesson, delete_lesson, \
    enroll_lesson, questions, create_question_container, update_question_container, create_text_question_container, \
    exercises, create_exercise_container, create_text_question,enroll_question_to_lesson, delete_question_container, \
    assign_text_questions_to_text_container,assign_text_questions_to_exercise_form, answer_exercise_question,select_exercise

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('student/<int:id>', student, name='student'),
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:id>', update_student, name='update_student'),
    path('delete_student/<int:id>', delete_student, name='delete_student'),
    path('courses', courses, name = 'courses'),
    path('course/<int:id>/', course, name='course'),
    path('create_course/', create_course, name='create_course'),
    path('update_course/<int:id>/', update_course, name='update_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),
    path('lessons/', lessons, name='lessons'),
    path('lesson/<int:id>/', lesson, name='lesson'),
    path('create_lesson/', create_lesson, name='create_lesson'),
    path('update_lesson/<int:id>/', update_lesson, name='update_lesson'),
    path('delete_lesson/<int:id>/', delete_lesson, name='delete_lesson'),
    path('enroll_student/', enroll_student, name='enroll_student'),
    path('enroll_lesson/', enroll_lesson, name='enroll_lesson'),
    path('enroll_question_to_lesson/', enroll_question_to_lesson, name='enroll_question_to_lesson'),
    path('exercises/', exercises, name='exercises'),
    path('create_exercise_container/', create_exercise_container, name='create_exercise_container'),
    path('questions/', questions, name='questions'),
    path('create_question_container/', create_question_container, name='create_question_container'),
    path('create_text_question_container/', create_text_question_container, name='create_text_question_container'),
    path('update_question_container/<int:id>', update_question_container, name='update_question_container'),
    path('delete_question_container/<int:id>', delete_question_container, name='delete_question_container'),
    path('create_text_question', create_text_question, name='create_text_question'),
    path('assign_text_questions_to_text_container', assign_text_questions_to_text_container,
         name='assign_text_questions_to_text_container'),
    path('assign_text_questions_to_exercise_form', assign_text_questions_to_exercise_form, name='assign_text_questions_to_exercise_form'),
    path('answer_exercise_question/<int:exercise_id>/answer/', answer_exercise_question, name='answer_exercise_question'),
    path('select_exercise', select_exercise, name='select_exercise')

]

