from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)


class Rating(models.Model):
    rating = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    message = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class News(models.Model):
    header = models.CharField(max_length=256)
    lan = models.CharField(max_length=5)
    message = models.TextField()
