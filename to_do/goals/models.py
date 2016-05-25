from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  monday = models.BooleanField(default=False)
  tuesday = models.BooleanField(default=False)
  wednesday = models.BooleanField(default=False)
  thursday = models.BooleanField(default=False)
  friday = models.BooleanField(default=False)
  saturday = models.BooleanField(default=False)
  sunday = models.BooleanField(default=False)