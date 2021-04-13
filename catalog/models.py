from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 2 - Модель производителя товара
# ============================
class Producer(models.Model):
    # Свойство модели
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
