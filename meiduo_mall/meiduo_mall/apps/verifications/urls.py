from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    #   r'^image_codes/(?P<uuid>[\w-]+)/$'
    url(r'^image_codes/(?P<uuid>[\w-]+)/$',views.ImageCodeView.as_view()),
]
