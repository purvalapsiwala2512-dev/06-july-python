from django.shortcuts import render,redirect
from dbapp.models import *
import os

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
  if request.method=='POST':  
    data = request.POST
    name = data.get("name")
    email =data.get("email")
    age = data.get("age")
    file = request.FILES.get("file")

    if id:
        st = Student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.age = age
        
        st.save()
        return render(request,"index.html",{"msg":"Update success"})
    else:
        Student.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{"msg":"Registration success"})


def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{"students":students})


def delete_student(request):
    id = request.GET.get("id")
    st = Student.objects.get(id=id)
    st.delete()
    return redirect("display")

def update_student(request):
    id = request.GET.get("id")
    st = Student.objects.get(id=id)
    return render(request,"index.html",{"st":st})


def product(request):
    data = request.POST
    name = data.get("name")
    price = data.get("price")
    qty = data.get("qty")
    Product.objects.create(name=name,price=price,qty=qty)
    return render(request,"product.html",{"msg":"Product added successfully"})