from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('single-project/<str:pk>', views.project, name="single-project" )
]
