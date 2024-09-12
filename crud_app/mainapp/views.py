from django.shortcuts import render
from .models import *

def showProductListView(request):
    products = Product.objects.all()
    context = {
        'Title' : 'Product | CRUD App',
        'CSS_File' : 'product.css'
    }
    return render(request, 'mainapp/productlist.html', {'context': context, 'products': products})

def showEditProductView(request):
    context = {
        'Title' : 'Edit Product | CRUD App',
        'CSS_File' : 'editproduct.css'
    }
    return render(request, 'mainapp/editproduct.html', {'context': context})

def showAddProductView(request):
    context = {
        'Title' : 'Add Product | CRUD App',
        'CSS_File' : 'addproduct.css'
    }
    return render(request, 'mainapp/addproduct.html', {'context': context})