from rest_framework.generics import get_object_or_404

from course.models import Course, Comment


def get_course(course_id):
    return get_object_or_404(Course.objects.get_all_courses(), id=course_id)


def like_comment(course, comment_id,  user):
    comment = get_object_or_404(course.comments, id=comment_id)
    comment.likes.add(user)
