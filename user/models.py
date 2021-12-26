from django.contrib.auth.models import AbstractUser
from django.db import models

from user.conf import DUPLICATE_EMAIL_ERROR_MESSAGE
from user.managers import UserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, blank=False, null=False,
                              error_messages={
                                  'unique': DUPLICATE_EMAIL_ERROR_MESSAGE,
                              })

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    image = models.ImageField(upload_to='users_images/', blank=True)

    def __str__(self):
        return self.email

    objects = UserManager()
