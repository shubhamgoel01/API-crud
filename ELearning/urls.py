from Icards.views import Icard
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from Icards import urls
from Icards import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls)),
]
