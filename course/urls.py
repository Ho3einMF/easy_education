from django.urls import path

from course.views import CourseListAPIView, CategoryListAPIView, CourseByCategoryAPIView, LessonsAPIView, \
    CourseByTeacherAPIView

app_name = 'course'
urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    # Filter Routes
    path('courses/category/<int:category_id>/', CourseByCategoryAPIView.as_view(), name='course-by-category'),
    path('courses/teacher/<int:teacher_id>/', CourseByTeacherAPIView.as_view(), name='course-by-teacher'),
    path('lessons/<int:course_id>/', LessonsAPIView.as_view(), name='course-lessons'),
]
