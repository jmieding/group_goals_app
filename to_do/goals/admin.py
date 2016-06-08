from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Goal

class ProfileInline(admin.TabularInline):
  model = Profile

class UserAdmin(BaseUserAdmin):
  inlines = (ProfileInline, )

class GoalAdmin(admin.ModelAdmin):
  model = Goal

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Goal, GoalAdmin)