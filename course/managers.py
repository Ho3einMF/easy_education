from django.core.cache import caches
from django.db import models

from course.conf import ALL_COURSES_TIMEOUT, COURSE_LESSON_SERIALIZER_TIMEOUT, ALL_CATEGORIES_TIMEOUT, \
    COURSE_COMMENTS_TIMEOUT

cache = caches['course']


class CourseManager(models.Manager):

    # using select_related and prefetch_related to handling
    # foreign keys and many to many fields in optimized mode.
    def get_all_courses(self):
        all_courses = cache.get('all_courses')
        if not all_courses:
            all_courses = self. \
               select_related('teacher', 'category'). \
               prefetch_related('hashtags', 'participants').filter(is_published=True)
            cache.set('all_courses', all_courses, ALL_COURSES_TIMEOUT)
        return all_courses

    def get_courses_by_category(self, category_id):
        return self.get_all_courses().filter(category_id=category_id)

    def get_courses_by_teacher(self, teacher_id):
        return self.get_all_courses().filter(teacher_id=teacher_id)

    def get_courses_by_user(self, user_id):
        return self.get_all_courses().filter(participants__in=[user_id])


class LessonManager(models.Manager):

    def get_lessons_of_course(self, course_id):

        lessons = cache.get('lessons')

        if lessons:
            if course_id in lessons:
                lessons_of_course = lessons[course_id]
            else:
                lessons_of_course = self.filter(course_id=course_id)
                lessons[course_id] = lessons_of_course
                cache.set('lessons', lessons, COURSE_LESSON_SERIALIZER_TIMEOUT)
        else:
            lessons_of_course = self.filter(course_id=course_id)
            lessons = {course_id: lessons_of_course}
            cache.set('lessons', lessons, COURSE_LESSON_SERIALIZER_TIMEOUT)

        return lessons_of_course


class TempLessonManager(models.Manager):

    def get_temp_lessons_by_teacher(self, user_id):
        return self.filter(user_id=user_id)


class CategoryManager(models.Manager):

    # using select_related to handling foreign key field in optimized mode.
    def get_all_categories(self):

        categories = cache.get('categories')

        if not categories:
            categories = self.select_related('parent')
            cache.set('categories', categories, ALL_CATEGORIES_TIMEOUT)

        return categories


class CommentManager(models.Manager):

    def get_course_comments(self, course_id):

        comments = cache.get('comments')

        if comments:
            if course_id in comments:
                comments_of_course = comments[course_id]
            else:
                comments_of_course = self.select_related('user'). \
                    prefetch_related('replies', 'likes', 'dislikes'). \
                    filter(course_id=course_id, hide=False, parent=None)
                comments[course_id] = comments_of_course
                cache.set('comments', comments, COURSE_COMMENTS_TIMEOUT)
        else:
            comments_of_course = self.select_related('user'). \
                prefetch_related('replies', 'likes', 'dislikes'). \
                filter(course_id=course_id, hide=False, parent=None)
            comments = {course_id: comments_of_course}
            cache.set('comments', comments, COURSE_COMMENTS_TIMEOUT)

        return comments_of_course
