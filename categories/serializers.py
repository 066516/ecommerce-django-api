# categories/serializers.py
from .models import Categories
from rest_framework import serializers
from products.models import Products

class CategoriesSerializer(serializers.ModelSerializer):
    # products = ProductsSerializer(many=True, read_only=True)  # Include related products

    class Meta:
        model = Categories  
        fields = ['id', 'name', 'created_at', 'updated_at',]
    def get_products(self, obj):
        from products.serializers import ProductsSerializer  # Delay the import
        return ProductsSerializer(obj.products.all(), many=True).data