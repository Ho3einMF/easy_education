from rest_framework import serializers

from course.models import Course, Category
from user.models import User


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'get_full_name', 'email']  # TODO => add image filed for user and also add in this serializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    hashtags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = '__all__'
