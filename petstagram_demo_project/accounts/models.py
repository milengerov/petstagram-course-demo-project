from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models


# after creating our user model, change in settings so Django to use this model, not the default Django AuthUserModel
from petstagram_demo_project.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    USERNAME_FIELD = "email"    # email will be used for login

    object = PetstagramUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to="profiles",
        blank=True,
    )
    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True
    )


from .signals import *