from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from user.models import User, Teacher
from user.utils import check_new_password, check_old_password


class SignupUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def validate_password2(self, value):
        return check_new_password(self.initial_data['password1'], value)

    def create(self, validated_data):
        return User.objects.create_user(email=self.validated_data['email'], password=self.validated_data['password2'])


class TokenSerializer(AuthTokenSerializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    username = email


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('id', 'user')

    def create(self, validated_data):
        instance = Teacher(**validated_data)
        instance.user = self.context['request'].user
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'image', 'teacher']
        extra_kwargs = {'email': {'read_only': True}}


class ChangePasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password1', 'password2')

    def validate_old_password(self, value):
        return check_old_password(user=self.context['request'].user, old_password=value)

    def validate_password2(self, value):
        return check_new_password(self.initial_data['password1'], value)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password1'])
        instance.save()
        return instance
