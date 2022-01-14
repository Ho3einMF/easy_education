from rest_framework import serializers

from course.models import Course, Category, Lesson, Comment
from course.utils import like_comment, check_status, dislike_comment
from user.serializers import UserProfileSerializer


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
    teacher = serializers.SerializerMethodField()
    category = CourseCategoryListSerializer(read_only=True)
    hashtags = serializers.StringRelatedField(many=True)

    @staticmethod
    def get_teacher(obj):
        return obj.teacher.get_full_name()

    class Meta:
        model = Course
        fields = '__all__'


class CourseByCategorySerializer(serializers.ModelSerializer):
    teacher = UserProfileSerializer(read_only=True)
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


class ReplyCommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'likes_count', 'dislikes_count', 'created_at')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    replies = ReplyCommentListSerializer(read_only=True, many=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'likes_count', 'dislikes_count', 'created_at', 'status', 'replies')

    def get_status(self, obj):
        return check_status(comment_obj=obj, user_id=self.context['request'].user.id)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'user', 'course')


class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('course', 'comment')

    def save(self):
        like_comment(self.validated_data['course'], self.validated_data['comment'], self.context['request'].user)


class CommentDislikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('course', 'comment')

    def save(self):
        dislike_comment(self.validated_data['course'], self.validated_data['comment'], self.context['request'].user)
