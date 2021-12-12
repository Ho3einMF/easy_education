# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from course.models import Course, Category, Lesson
from course.serializers import CourseListSerializer, LessonSerializer, SubCategorySerializer, \
    CourseByCategorySerializer, CourseByTeacherSerializer


class CategoryListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SubCategorySerializer
    queryset = Category.objects.get_all_categories()


class CourseListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseListSerializer
    queryset = Course.objects.get_all_courses()


class CourseByCategoryAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseByCategorySerializer

    def get_queryset(self):
        return Course.objects.get_courses_by_category(self.kwargs['category_id'])


class CourseByTeacherAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseByTeacherSerializer

    def get_queryset(self):
        return Course.objects.get_courses_by_teacher(self.kwargs['teacher_id'])


class LessonsAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.get_lessons_of_course(self.kwargs['course_id'])
