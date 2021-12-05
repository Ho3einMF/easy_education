from django.db import models


class CourseManager(models.Manager):

    # using select_related and prefetch_related to handling
    # foreign keys and many to many fields in optimized mode.
    def get_all_courses(self):
        return self. \
               select_related('teacher'). \
               select_related('category'). \
               prefetch_related('hashtags').filter(is_published=True)

    def get_courses_by_category(self, category_id):
        return self.get_all_courses().filter(category_id=category_id)


class LessonManager(models.Manager):

    def get_lessons_of_course(self, course_id):
        return self.filter(course_id=course_id)


class CategoryManager(models.Manager):

    def get_all_categories(self):
        return self.select_related('parent')
