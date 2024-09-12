from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.showProductListView, name="product-list"),
    path("add-product/", views.showAddProductView, name="add-product"),
    path("edit-product/", views.showEditProductView, name="edit-list"),
]