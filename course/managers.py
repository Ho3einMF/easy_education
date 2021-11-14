from django.db import models


class CourseManager(models.Manager):

    # using select_related and prefetch_related to handling
    # foreign keys and many to many fields in optimized mode.
    def get_all_courses(self):
        return self. \
               select_related('teacher'). \
               select_related('category'). \
               prefetch_related('hashtags').filter(is_published=True)
