from rest_framework.generics import get_object_or_404

from course.models import Course


def get_course(course_id):
    return get_object_or_404(Course.objects.get_all_courses(), id=course_id)


def like_comment(course, comment_id,  user):
    comment = get_object_or_404(course.comments, id=comment_id)
    if check_status(comment_obj=comment, user_id=user.id) == 'disliked':
        comment.dislikes.remove(user)
    comment.likes.add(user)


def dislike_comment(course, comment_id,  user):
    comment = get_object_or_404(course.comments, id=comment_id)
    if check_status(comment_obj=comment, user_id=user.id) == 'liked':
        comment.likes.remove(user)
    comment.dislikes.add(user)


def check_status(comment_obj, user_id):
    """
    if user already liked that comment => status = liked
    else if user already disliked that comment => status = disliked
    else => status = null
    """

    for like in comment_obj.likes.all():
        if user_id == like.id:
            return 'liked'
    for dislike in comment_obj.dislikes.all():
        if user_id == dislike.id:
            return 'disliked'
    return None
