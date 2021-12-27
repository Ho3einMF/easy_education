from django.contrib import admin

# Register your models here.
from course.models import Course, Lesson, Category, Hashtag, Comment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(Comment)
