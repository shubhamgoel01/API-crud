from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Add_category/',views.Icard.as_view()),
    path('Add_category/<int:pk>/',views.Icard.as_view()),

]
