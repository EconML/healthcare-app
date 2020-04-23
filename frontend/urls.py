from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.conditionlist, name='condition_list'),

]
