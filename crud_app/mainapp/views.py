from django.shortcuts import render, redirect
from .models import *
from .utils import *
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages

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
        productname = request.POST[PRODUCT_NAME]
        category = request.POST[PRODUCT_CATEGORY]
        quantity = int(request.POST[PRODUCT_CATEGORY])
        price = float(request.POST[PRODUCT_PRICE])
        image = request.FILES.get(PRODUCT_IMAGE)
        
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
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return redirect("product-list")

    if request.method == "POST":
        productname = request.POST.get(PRODUCT_NAME)
        category = request.POST.get(PRODUCT_CATEGORY)
        quantity = int(request.POST.get(PRODUCT_QUANTITY))
        price = float(request.POST.get(PRODUCT_PRICE))
        image = request.FILES.get(PRODUCT_IMAGE)

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

def showLoginPageView(request):
    context = {
        'Title': 'Login | CRUD App',
        'CSS_File': 'login.css'
    }
    return render(request, 'mainapp/login.html', context)

def showSignUpPageView(request):
    
    if request.method == "POST":
        firstName = request.POST.get(FIRST_NAME)
        lastName = request.POST.get(LAST_NAME)
        emailAddress = request.POST.get(EMAIL_ADDRESS)
        username = request.POST.get(USERNAME)
        password = request.POST.get(PASSWORD)
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already existed!")
            return redirect("user-signup")
        
        newUser = User.objects.create(
            first_name = firstName,
            last_name = lastName,
            email = emailAddress,
            username = username,
        )
        newUser.set_password(password)
        newUser.save()
        messages.success(request, "Account created successfully!")
        
        return redirect("user-login")   
         
    context = {
        'Title': 'SignUp | CRUD App',
        'CSS_File': 'signup.css'
    }
    return render(request, 'mainapp/signup.html', context)
