from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.showProductListView, name="product-list"),
    path("user-login/", views.showLoginPageView, name="user-login"),
    path("user-signup/", views.showSignUpPageView, name="user-signup"),
    path("products/", views.showProductListView, name="product-list"),
    path("products/add-product/", views.showAddProductView, name="add-product"),
    path("products/edit-product/<int:id>", views.showEditProductView, name="edit-product"),
    path("products/delete-product/<int:id>", views.deleteProduct, name="delete-product"),
    path("user-logout/", views.userLogout, name="user-logout"),
    path("products/search/", views.searchProduct, name="search-product"),
    path("products/sort/", views.sortProduct, name="sort-product"),
]

