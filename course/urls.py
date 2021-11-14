from django.urls import path

from course.views import CourseListAPIView

app_name = 'course'
urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
]
