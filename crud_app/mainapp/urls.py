from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.showProductListView, name="product-list"),
    path("products/", views.showProductListView, name="product-list"),
    path("products/add-product/", views.showAddProductView, name="add-product"),
    path("products/edit-product/<int:id>", views.showEditProductView, name="edit-product"),
    path("delete-product/<int:id>", views.deleteProduct, name="delete-product"),
]