# app/lessons/urls.py
from django.urls import path
from app.lessons.views import LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = 'lessons'

urlpatterns = [
    path('', LessonListAPIView.as_view()),
    path('create/', LessonCreateAPIView.as_view()),
    path('<int:pk>/', LessonRetrieveAPIView.as_view()),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view()),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view()),
]