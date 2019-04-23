from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
# 注册
    url(r'^register/$', RegisteView.as_view(),name='register'),
# 判断用户名是否已注册
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$',usernameCountView.as_view()),
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$',mobileCountView.as_view()),
]