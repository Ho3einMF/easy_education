from django.contrib.auth import password_validation
from django.http import Http404

from rest_framework import serializers

from user.conf import PASSWORDS_MATCH_MESSAGE, OLD_PASSWORD_MESSAGE
from user.models import User


def check_new_password(password1, password2, user=None):
    if (password1 and password2) and (password1 != password2):
        raise serializers.ValidationError({"detail": PASSWORDS_MATCH_MESSAGE})

    password_validation.validate_password(password2, user)
    return password2


def check_old_password(user, old_password):
    if user.check_password(old_password):
        return old_password
    raise serializers.ValidationError({"detail": OLD_PASSWORD_MESSAGE})


def get_user_or_404(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Http404()
