from django.contrib.auth import password_validation
from django.http import Http404
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from user.models import User


def check_new_password(password1, password2, user=None):
    if (password1 and password2) and (password1 != password2):
        raise serializers.ValidationError(_('Passwords do not match'))

    password_validation.validate_password(password2, user)
    return password2


def get_user_or_404(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist as e:
        return Http404()

