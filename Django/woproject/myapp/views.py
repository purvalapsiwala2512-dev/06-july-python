from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    return render(request,"display.html")

def register(request):
     if request.method=='POST':
        data = request.POST
        id = data.get("id")
        country = data.get("country")
        days = data.get("days")
        cost = data.get("cost")
        
        if id :
            product = Travel.objects.get(id = id)
            product.name = name
            product.price = price
            product.qty = qty
            product.save()
            msg = "Update successfully"
        else:
            Product.objects.create(name=name,price=price,qty=qty)
            msg= "Registration successfully !!"
    return render(request,"index.html",{"msg":msg})

def delete_travel(request):
    id = request.GET.get("id")
    product = Travel.objects.get(id = id)
    product.delete()
    return redirect("display")
