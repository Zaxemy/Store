from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        
    def __str__(self):
        return f'{self.name} | {self.category}'