from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import NewUserForm, MyLoginForm

import datetime


@login_required(login_url='goals/login/')
def index(request):
  users = User.objects.all() #.exclude(username = 'jtmieding')
  day = datetime.datetime.today().weekday()
  return render(request, 'goals/base_goals.html', {'users': users, 'day':day})

def update(request, day):
  if request.user.is_authenticated():
    day_value = getattr(request.user.profile, day)
    if day_value == False:
      setattr(request.user.profile, day, True)
    else:
      setattr(request.user.profile, day, False)
    request.user.profile.save()
  else:
    print "User not Authenticated"
  return HttpResponseRedirect('/goals')

@csrf_exempt
def register(request):
  form = NewUserForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      new_user = User.objects.create_user(username, email=None, password=password)
      new_profile = Profile.objects.create(user=new_user)
      user = authenticate(username=username, password=password)
      print user
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/goals')
        else:
          print "NOT ACTIVE"
      else:
        print "Invalid Password"
    else:
      print "INVALID FORM"
  return render(request, 'register.html', {'form':form})

@csrf_exempt
def login_user(request):
  form = MyLoginForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      print user
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/goals')
        else:
          print "USER NOT ACTIVE"
      else:
        print "INVALID LOGIN"
        print form.errors
        return render(request, 'login.html', {'form':form})
    else:
      print "INVALID FORM"
  return render(request, 'login.html', {'form':form})

def logout_user(request):
  logout(request)
  return HttpResponseRedirect('/')
