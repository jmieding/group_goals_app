from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  monday = models.BooleanField(default=False)
  tuesday = models.BooleanField(default=False)
  wednesday = models.BooleanField(default=False)
  thursday = models.BooleanField(default=False)
  friday = models.BooleanField(default=False)
  saturday = models.BooleanField(default=False)
  sunday = models.BooleanField(default=False)

  def __str__(self):
    return self.user

class Goal(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  # days_complete = models.IntegerField(default=0)
  # weeks_complete = models.IntegerField(default=0)
  # consecutive_days = models.IntegerField(default=0)
  # current_streak = models.IntegerField(default=0)
  monday = models.BooleanField(default=False)
  tuesday = models.BooleanField(default=False)
  wednesday = models.BooleanField(default=False)
  thursday = models.BooleanField(default=False)
  friday = models.BooleanField(default=False)
  saturday = models.BooleanField(default=False)
  sunday = models.BooleanField(default=False)

  def __str__(self):
    return self.title