from django import forms
from .models import Goal

class NewUserForm(forms.Form):
  username = forms.CharField(label='Name', max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Name', 'class':'form-control', 'id':'username'}))
  password = forms.CharField(label='Password', max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control password', 'type':'password'}))
  password2 = forms.CharField(label='Password', max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control password', 'type':'password'}))
  #remember_me = forms.BooleanField(label='Checkbox', widget=forms.CheckboxInput(attrs={'value':'remember-me'}))

class MyLoginForm(forms.Form):
  username = forms.CharField(label='Name', max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Name', 'class':'form-control', 'id':'username'}))
  password = forms.CharField(label='Password', max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control', 'id':'password', 'type':'password'}))
  #remember_me = forms.BooleanField(label='Checkbox', widget=forms.CheckboxInput(attrs={'value':'remember-me'}))

class GoalForm(forms.ModelForm):
  class Meta:
    model = Goal
    fields = ['title', 'description']