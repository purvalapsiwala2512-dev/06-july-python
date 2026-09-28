from django.shortcuts import render
from ytapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")



def display(request):
    customers = Customer.objects.all()
    return render(request,"display.html",{"customers":customers})
