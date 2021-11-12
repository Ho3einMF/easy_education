from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from user.models import User
from user.utils import check_new_password


class SignupUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

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
