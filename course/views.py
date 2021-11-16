# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from course.models import Course, Category
from course.serializers import CourseSerializer, CategorySerializer


class CourseListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer
    queryset = Course.objects.get_all_courses()


class CategoryListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseByCategory(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.get_courses_by_category(self.kwargs['category_id'])
