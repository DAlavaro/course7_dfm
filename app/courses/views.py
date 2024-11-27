# app/courses/views.py
from rest_framework import viewsets
from app.courses.serializers import CourseSerializer, Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
