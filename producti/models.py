from django.db import models

# Create your models here.


class Product(models.Model):
    # id = models.AutoField() --> default , primary key
    title = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    discount = models.BooleanField(default=True)
