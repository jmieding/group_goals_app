from django.conf.urls import include, url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'login/', views.login_user, name='login_user'),
  url(r'logout/', views.logout_user, name='logout_user'),
  url(r'register/', views.register, name='register'),
  url(r'^(?P<day>[\w]+)/$', views.update, name='update'),
]