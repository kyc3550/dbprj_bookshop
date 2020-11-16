from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import *

def book_list(request):
    books = Product.objects.all()
    return render(request,'shop/index.html',{'books':books})

def product_detail(request,book_num):
    product = get_object_or_404(Product, book_num=book_num)
    return render(request, 'shop/detail.html', {'product':product})
