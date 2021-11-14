# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from course.models import Course
from course.serializers import CourseSerializer


class CourseListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer
    queryset = Course.objects.get_all_courses()
