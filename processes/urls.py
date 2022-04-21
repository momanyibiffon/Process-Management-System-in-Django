from django.contrib import admin
from django.urls import path
from . import views

app_name = 'processes' 

urlpatterns = [
    path('', views.index_view, name="index"),
    path('process', views.single_process_view, name="single_process"),
    path('suspend_process', views.suspend_process_view, name="suspend"),
    path('resume_process', views.resume_process_view, name="resume"),
    path('terminate_process', views.terminate_process_view, name="terminate")
]
