from rest_framework.generics import get_object_or_404

from course.models import Course


def get_course(course_id):
    return get_object_or_404(Course.objects.get_all_courses(), id=course_id)
