from django.urls import *
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("register",register,name="register"),
    path("delete",delete_travel,name="delete"),
]