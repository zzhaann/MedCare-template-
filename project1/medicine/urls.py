from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', home),
    re_path(r'^contact/$', contact),
    re_path(r'^about/$', about),
    re_path(r'^service/$', service),
    re_path(r'^remedy/$', remedy),
]
