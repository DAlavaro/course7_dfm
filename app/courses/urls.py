# app/courses/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.courses.views import CourseViewSet

app_name = 'courses'

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = router.urls