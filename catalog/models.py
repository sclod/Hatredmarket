from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Producer(models.Model):
    # Свойство модели
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='pictures/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id',),)

    def __str__(self):
        return self.name
