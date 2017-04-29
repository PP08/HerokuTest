from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

