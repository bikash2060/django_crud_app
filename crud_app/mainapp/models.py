from django.db import models

class ProductCategory(models.Model):  
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=200)
    productImage = models.FileField(null=True, blank=True)  
    stockQuantity = models.IntegerField()
    productPrice = models.FloatField()  
    categoryName = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="category")  

    def __str__(self):
        return self.productName
