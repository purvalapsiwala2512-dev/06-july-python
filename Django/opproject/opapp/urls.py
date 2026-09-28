from django.urls import *
from opapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("register",register,name="register"),
    path("delete",delete_product,name="delete"),
    
]