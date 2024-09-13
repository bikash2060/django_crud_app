from django.shortcuts import render, redirect
from .models import *
from .utils import *

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

def showEditProductView(request, id):
    context = {
        'Title' : 'Edit Product | CRUD App',
        'CSS_File' : 'editproduct.css'
    }
    return render(request, 'mainapp/editproduct.html', context)

def deleteProduct(request, id):
    return 1