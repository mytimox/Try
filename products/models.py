from django.db import models

# Create your models here

class Product(models.Model):

    name = models.CharField(max_length=22, verbose_name="Ім'я")
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        st = "{}, {}".format(self.price, self.name)
        return st
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        st = '{}'.format(self.id) 
        return st
    class Meta:
        verbose_name = 'Світлина'
        verbose_name_plural = 'Світлини'