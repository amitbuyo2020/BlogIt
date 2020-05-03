from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email Address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=250, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name="Profile Picture")
    current_location = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
