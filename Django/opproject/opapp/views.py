from django.shortcuts import render,redirect
from opapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")


def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})

def register(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")

        Product.objects.create(name=name,price=price,qty=qty)

        return render(request,"index.html")


    def delete_product(request):
        id = request.GET.get("id")
        product = Product.objects.get(id = id)
        product.delete()
        return redirect("display")
