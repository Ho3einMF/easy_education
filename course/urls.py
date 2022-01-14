from django.urls import path

from course.views import CourseListAPIView, CategoryListAPIView, CourseByCategoryAPIView, LessonsAPIView, \
    CourseByTeacherAPIView, JoinToCourse, CoursesByUserAPIView, CommentListAPIView, CommentCreate, CommentLikeAPIView, \
    CommentDislikeAPIView

app_name = 'course'
urlpatterns = [
    # **Courses**

    # list of all courses
    path('courses/', CourseListAPIView.as_view(), name='course-list'),

    # filtering courses

    # by category
    path('courses/category/<int:category_id>/', CourseByCategoryAPIView.as_view(), name='course-by-category'),
    # by teacher (list of courses held by the teacher)
    path('courses/teacher/<int:teacher_id>/', CourseByTeacherAPIView.as_view(), name='course-by-teacher'),
    # by user (list of courses that the user has participated in)
    path('courses/user/', CoursesByUserAPIView.as_view(), name='course-by-user'),

    # join to course
    path('course/join/<int:course_id>/', JoinToCourse.as_view(), name='course-join'),

    # **Category**
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    # **Lessons**
    path('lessons/<int:course_id>/', LessonsAPIView.as_view(), name='course-lessons'),

    # **Comments**

    # list of comments by course
    path('comments/<int:course_id>/', CommentListAPIView.as_view(), name='comment-list'),

    # post comment on a course
    path('comment/create/', CommentCreate.as_view(), name='comment-create'),

    # like a comment
    path('comment/like/', CommentLikeAPIView.as_view(), name='comment-like'),

    # dislike a comment
    path('comment/dislike/', CommentDislikeAPIView.as_view(), name='comment-like')
]
