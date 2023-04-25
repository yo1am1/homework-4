from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('generate-student/', views.generate_student, name='generate-student'),
    path('generate-students/', views.generate_students, name='generate-students'),
    path('', views.index, name='index'),
]
