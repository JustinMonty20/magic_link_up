from django.db import models

# Create your models here.

# creating my model to add into the database.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    key_word = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    
