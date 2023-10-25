from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField(max_length=10, default=0)

# Create your models here.
