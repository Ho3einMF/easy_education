from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    phone_number = PhoneNumberField(unique=True)
    scanned_national_card = models.ImageField(upload_to='national_cards/')
    scanned_birth_certificate = models.ImageField(upload_to='birth_certificate/')
    resume = models.FileField(upload_to='resume/')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
