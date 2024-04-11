from django.db import models

# Create your models here.

# data/models.py

from django.db import models
from django.contrib.auth.models import User

class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=140, blank=True)
    location = models.CharField(max_length=140, blank=True)
    website = models.URLField(max_length=200, blank=True)

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    expiration = models.DateTimeField()

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    expiration = models.DateTimeField()
    verified = models.BooleanField(default=False)

