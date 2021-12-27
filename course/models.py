from django.db import models
from django.utils.timezone import now

from course.managers import CourseManager, LessonManager, CategoryManager, CommentManager
from user.models import User


class Hashtag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories_images/', blank=True)

    # Foreign key (for handling sub category)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    # Manager
    objects = CategoryManager()

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses_images/')
    short_description = models.TextField(blank=False, max_length=60)
    description = models.TextField(blank=False)
    price = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    # Foreign keys
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='courses')

    # Many to many
    hashtags = models.ManyToManyField(Hashtag, related_name='courses')
    participants = models.ManyToManyField(User, blank=True, related_name='participants')

    # Manager
    objects = CourseManager()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='lesson_video/')
    lesson_files = models.FileField(upload_to='lesson_files/', blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    # Foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    # Manager
    objects = LessonManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, related_name='dislikes')
    hide = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    # Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    # for handling replies comments
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    # Manager
    objects = CommentManager()

    def __str__(self):
        return f'email: {self.user.email} | course: {self.course.title}'

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()
