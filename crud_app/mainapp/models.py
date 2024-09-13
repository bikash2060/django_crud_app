from django.db import models

class Product(models.Model):
    category = [
        ('LP', 'Laptop'),
        ('SP', 'Smartphone'),
        ('TB', 'Tablet'),
        ('SW', 'Smartwatch'),
        ('HP', 'Headphones'),
    ]    
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    ProductPrice = models.FloatField()  
    StockQuantity = models.IntegerField()
    ProductCategory = models.CharField(max_length=2, choices=category)
    ProductImage = models.ImageField(upload_to="product_images/", max_length=200, null=True)  

    def __str__(self):
        return self.ProductName
