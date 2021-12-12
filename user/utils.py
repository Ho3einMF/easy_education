from django.contrib.auth import password_validation
from django.http import Http404
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from user.models import User


def check_new_password(password1, password2, user=None):
    if (password1 and password2) and (password1 != password2):
        raise serializers.ValidationError(_("Password fields didn't match."))

    password_validation.validate_password(password2, user)
    return password2


def check_old_password(user, old_password):
    if user.check_password(old_password):
        return old_password
    raise serializers.ValidationError({"detail": "Old password is not correct"})


def get_user_or_404(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Http404()
