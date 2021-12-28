# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.conf import COMMENT_LIKE_MESSAGE, COMMENT_DISLIKE_MESSAGE
from course.models import Course, Category, Lesson, Comment
from course.serializers import CourseListSerializer, LessonSerializer, SubCategorySerializer, \
    CourseByCategorySerializer, CourseByTeacherSerializer, CoursesByUserSerializer, CommentListSerializer, \
    CommentCreateSerializer, CommentLikeSerializer, CommentDislikeSerializer
from course.utils import get_course


class CategoryListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SubCategorySerializer
    queryset = Category.objects.get_all_categories()


class CourseListAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseListSerializer
    queryset = Course.objects.get_all_courses()


class CourseByCategoryAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseByCategorySerializer

    def get_queryset(self):
        return Course.objects.get_courses_by_category(self.kwargs['category_id'])


class CourseByTeacherAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = CourseByTeacherSerializer

    def get_queryset(self):
        return Course.objects.get_courses_by_teacher(self.kwargs['teacher_id'])


class LessonsAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.get_lessons_of_course(self.kwargs['course_id'])


class JoinToCourse(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, **kwargs):
        course = get_course(kwargs['course_id'])
        course.participants.add(request.user)
        return Response()


class CoursesByUserAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CoursesByUserSerializer

    def get_queryset(self):
        return Course.objects.get_courses_by_user(self.request.user.id)


class CommentListAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.get_course_comments(self.kwargs['course_id'])


class CommentCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentLikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        serializer = CommentLikeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': COMMENT_LIKE_MESSAGE}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDislikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        serializer = CommentDislikeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': COMMENT_DISLIKE_MESSAGE}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
