from django.db import models

class Product(models.Model):
    
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    ProductPrice = models.FloatField()  
    StockQuantity = models.IntegerField()
    ProductCategory = models.CharField(max_length=100)
    ProductImage = models.ImageField(upload_to="", max_length=200, null=True)  

    def __str__(self):
        return self.ProductName
