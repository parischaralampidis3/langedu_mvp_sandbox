from django.urls import path
from ..views import questions, update_question_container, create_question_container,answer_exercise_question,\
    delete_question_container,create_text_question,assign_text_questions_to_text_container, create_text_question_container, assign_text_questions_to_exercise_form


urlpatterns = [
    path('questions', questions, name='questions'),
    path('<int:id>/', update_question_container, name='update_question_container'),
    path('create_lesson', create_question_container, name='create_question_container'),
    path('answer_exercise_question', answer_exercise_question, name='answer_exercise_question'),
    path('<int:id>', delete_question_container, name='delete_question_container'),
    path('create_text_question',create_text_question, name='create_text_question'),
    path('assign_text_questions_to_text_container', assign_text_questions_to_text_container, name="assign_text_questions_to_text_container"),
    path('create_text_question_container', create_text_question_container, name="create_text_question_container"),
    path('assign_text_questions_to_exercise_form', assign_text_questions_to_exercise_form, name='assign_text_questions_to_exercise_form')


]