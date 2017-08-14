from django.db import models
from products.models import Product

# Create your models here

class Status(models.Model):

    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        st = '{}'.format(self.name)
        return st
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси до замовлення'

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all product in order
    customer_name = models.CharField(max_length=22, verbose_name="Ім'я")
    customer_last_name = models.CharField(max_length=33, verbose_name='Прізвище')
    customer_email = models.EmailField(verbose_name='E-mail', default=None)
    customer_phone = models.CharField(max_length=13, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=300, blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        st = "Замовлення {} {}".format(self.id, self.status.name)
        return st
    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)  #proce*num
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        st = '{}'.format(self.product.name)
        return st
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'