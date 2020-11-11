from django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('e/getusers', views.UserList.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)
