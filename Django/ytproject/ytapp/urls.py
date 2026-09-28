from django.urls import path
from ytapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
]