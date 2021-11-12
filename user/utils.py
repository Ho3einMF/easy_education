from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


def check_new_password(password1, password2, user=None):
    if (password1 and password2) and (password1 != password2):
        raise serializers.ValidationError(_('Passwords do not match'))

    password_validation.validate_password(password2, user)
    return password2

