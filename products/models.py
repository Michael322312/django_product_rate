from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 63)
    info = models.TextField()
    price = models.DecimalField(decimal_places = 1, max_digits = 1000)

class Rate(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="ratings")
    author = models.CharField(max_length = 63)
    text = models.TextField()
    rating = models.DecimalField(decimal_places = 1, max_digits = 2)
    
    class Meta:
        ordering = ["-id"]