from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    data = request.POST
    id = data.get("id")
    name = data.get("name")
    duration = data.get("duration")
    fees = data.get("fees")

    if id:
        st = Course.objects.get(pk=id)
        st.name = name
        st.duration = duration
        st.fees = fees
        st.save()
        return render(request,"index.html",{"msg":"Update success"})
    else:
        Course.objects.create(name=name,duration=duration,fees=fees)
        return render(request,"index.html",{"msg":"Registration successful"})

def display(request):
    course = Course.objects.all()
    return render(request,"display.html",{"courses":course})


def delete_course(request):
    id = request.GET.get("id")
    st = Course.objects.get(id=id)
    st.delete()
    return redirect("display")

def update_course(request):
    id = request.GET.get("id")
    st = Course.objects.get(id=id)
    return render(request,"index.html",{"st":st})