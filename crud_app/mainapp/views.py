from django.shortcuts import render

def showProductListView(request):
    context = {
        'Title' : 'Product | CRUD App',
        'CSS_File' : 'product.css'
    }
    return render(request, 'mainapp/productlist.html', {'context': context})

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