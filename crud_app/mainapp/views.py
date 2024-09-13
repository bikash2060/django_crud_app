from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .utils import *

def custom_error_page(request, exception):
    context = {
        'Title' : 'Page Not Found',
        'CSS_File' : 'errorpage.css',
    }
    return render(request, 'mainapp/errorpage.html', context)


def showProductListView(request):
    products = Product.objects.all()
    context = {
        'Title' : 'Product | CRUD App',
        'CSS_File' : 'product.css',
        'products': products
    }
    return render(request, 'mainapp/productlist.html', context)

def showAddProductView(request):
    if request.method == "POST":
        # Retrieve data from the user
        productname = request.POST[productName]
        category = request.POST[productCategory]
        quantity = int(request.POST[productQuantity])
        price = float(request.POST[productPrice])
        image = request.FILES.get(productImage)
        
        # Create the Product Instance
        newProduct = Product.objects.create(
            ProductName = productname, 
            ProductImage = image,
            StockQuantity = quantity,
            ProductPrice = price,
            ProductCategory = category
        )
        newProduct.save()
        
        return redirect("product-list")              
        
    context = {
        'Title' : 'Add Product | CRUD App',
        'CSS_File' : 'addproduct.css'
    }
    return render(request, 'mainapp/addproduct.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def showEditProductView(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return redirect("product-list")

    if request.method == "POST":
        productname = request.POST.get("productName")
        category = request.POST.get("category")
        quantity = int(request.POST.get("quantity"))
        price = float(request.POST.get("price"))
        image = request.FILES.get("image")
        print(image)

        product.ProductName = productname
        if category:
            product.ProductCategory = category
        product.StockQuantity = quantity
        product.ProductPrice = price
        if image:
            product.ProductImage = image

        product.save()
        return redirect("product-list")

    context = {
        'Title': 'Edit Product | CRUD App',
        'CSS_File': 'editproduct.css',
        'product': product
    }
    return render(request, 'mainapp/editproduct.html', context)

def deleteProduct(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return redirect("product-list")
    
    product.delete()
    
    return redirect("product-list")