from django.db import models

# Create your models here

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        st = "{}" .format(self.name)
        return st
    class Meta:
        verbose_name = 'Категорія товару'
        verbose_name_plural = 'Категорія товарів'

class Product(models.Model):

    name = models.CharField(max_length=22, verbose_name="Ім'я")
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=0)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=' ')
    is_active = models.BooleanField(default=True)   
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
    is_main = models.BooleanField(default=False)    
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        st = '{}'.format(self.id) 
        return st
    class Meta:
        verbose_name = 'Світлина'
        verbose_name_plural = 'Світлини'