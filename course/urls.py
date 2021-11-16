from django.urls import path

from course.views import CourseListAPIView, CategoryListAPIView

app_name = 'course'
urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
]
