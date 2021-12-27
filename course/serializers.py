from rest_framework import serializers

from course.models import Course, Category, Lesson
from user.serializers import TeacherSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class SubCategorySerializer(serializers.ModelSerializer):
    parent = CategorySerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'parent')


class CourseCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image')


class CourseListSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    category = CourseCategoryListSerializer(read_only=True)
    hashtags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseByCategorySerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    hashtags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseByTeacherSerializer(serializers.ModelSerializer):
    category = CourseCategoryListSerializer(read_only=True)
    hashtags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class CoursesByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'image')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('course',)
