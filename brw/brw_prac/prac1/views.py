from django.shortcuts import render, redirect
from.models import Product

def list(request):
    return render(request,'list.html')

def main(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('price')
        product = Product(title=title,price=price,description=description)
        product.save()
        redirect('list')
    return render(request, 'main.html')

def holy(request):
    return render(request, 'holy.html')
# Create your views here.


