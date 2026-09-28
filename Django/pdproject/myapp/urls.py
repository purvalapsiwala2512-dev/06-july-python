from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete_course,name="delete"),
    path("update",update_course,name="update")
]