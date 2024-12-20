from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    category = models.ForeignKey('categories.Categories', on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
