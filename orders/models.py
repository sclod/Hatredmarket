from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from catalog.models import Product


class Orders(models.Model):

    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='pictures/')

    def __str__(self):
        return str(self.name)
