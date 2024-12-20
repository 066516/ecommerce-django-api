#products/serializers.py
from .models import Products
from rest_framework import serializers
# from categories.serializers import CategoriesSerializer
from categories.models import Categories
class ProductsSerializer(serializers.ModelSerializer):
    # category = CategoriesSerializer(read_only=True)  # Use nested serializer for category
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'category', 'created_at', 'updated_at',]
    def get_category(self, obj):
        from categories.serializers import CategoriesSerializer  # Delay the import
        return CategoriesSerializer(obj.category).data