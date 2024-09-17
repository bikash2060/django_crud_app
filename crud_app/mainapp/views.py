from django.shortcuts import render, redirect
from .models import *
from .utils import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def custom_error_page(request, exception):
    context = {
        'Title' : 'Page Not Found',
        'CSS_File' : 'errorpage.css',
    }
    return render(request, 'mainapp/errorpage.html', context)

@login_required(login_url="user-login/")
def showProductListView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'mainapp/productlist.html', context)

@login_required(login_url="user-login/")
def showAddProductView(request):
    if request.method == "POST":
        # Retrieve data from the user
        productname = request.POST[PRODUCT_NAME]
        category = request.POST[PRODUCT_CATEGORY]
        quantity = int(request.POST[PRODUCT_QUANTITY])
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

    return render(request, 'mainapp/addproduct.html')

@login_required(login_url="user-login/")
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
        'product': product
    }
    return render(request, 'mainapp/editproduct.html', context)

@login_required(login_url="user-login/")
def deleteProduct(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return redirect("product-list")
    
    product.delete()
    
    return redirect("product-list")

def showLoginPageView(request):
    if request.user.is_authenticated:
        return redirect("product-list")
    
    if request.method == "POST":
        username = request.POST.get(USERNAME)
        password = request.POST.get(PASSWORD)
        
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("product-list")
            else:
                messages.error(request, "Invalid password!", {'username': username})
                return redirect("user-login")           
        else:
            messages.error(request, "User does not exist!")
            return redirect("user-login")
    
    return render(request, 'mainapp/login.html')

def showSignUpPageView(request):
    if request.user.is_authenticated:
        return redirect("product-list") 
    
    if request.method == "POST":
        firstName = request.POST.get(FIRST_NAME)
        lastName = request.POST.get(LAST_NAME)
        emailAddress = request.POST.get(EMAIL_ADDRESS)
        username = request.POST.get(USERNAME)
        password = request.POST.get(PASSWORD)
        retypePassword = request.POST.get(RETYPED_PASSWORD)
        
        # Check for existing email
        if User.objects.filter(email=emailAddress).exists():
            messages.error(request, "Email address already exists!")
            return render(request, 'mainapp/signup.html', {
                'firstName': firstName,
                'lastName': lastName,
                'emailAddress': emailAddress,
                'username': username,
            })

        # Check for existing username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'mainapp/signup.html', {
                'firstName': firstName,
                'lastName': lastName,
                'emailAddress': emailAddress,
                'username': username,
            })

        # Check if passwords match
        if password != retypePassword:
            messages.error(request, "Passwords do not match!")
            return render(request, 'mainapp/signup.html', {
                'firstName': firstName,
                'lastName': lastName,
                'emailAddress': emailAddress,
                'username': username,
            })
        
        newUser = User.objects.create(
            first_name = firstName,
            last_name = lastName,
            email = emailAddress,
            username = username,
        )
        newUser.set_password(password)
        newUser.save()
        messages.success(request, "Account created successfully!")
        
        return redirect("user-signup")   
         
    return render(request, 'mainapp/signup.html')

def userLogout(request):
    logout(request)
    return redirect("user-login")