from django.shortcuts import render

# Create your views here.
from .models import Products

from .serializers import ProductsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from categories.models import Categories
from categories.serializers import CategoriesSerializer
class ProductsListView(APIView):
    def get(self, request):
        try:
            products = Products.objects.all()
            serializer = ProductsSerializer(products, many=True)
            return Response({"Products": serializer.data})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ProductsCreateView(APIView):
    def post(self, request):
        try:
            serializer = ProductsSerializer(data=request.data)
            if serializer.is_valid():
                # Validate category existence
                category_id = request.data.get('category')
                category = get_object_or_404(Categories, id=category_id)  # Handles 404 automatically
                
                # Save product with category
                serializer.save(category=category)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ProductsDetail(APIView):
    def get(self, request, product_id):
        try:
            # Get the product or return 404 if not found
            product = get_object_or_404(Products, id=product_id)
            
            # Serialize the product data
            product_serializer = ProductsSerializer(product)
            
            # Get the associated category and serialize it
            category = product.category
            category_serializer = CategoriesSerializer(category)

            # Combine both product and category data
            response_data = product_serializer.data
            response_data['category'] = category_serializer.data

            return Response(response_data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, product_id):
        try:
            product = get_object_or_404(Products, id=product_id)
            product.delete()
            return Response({"message": "products deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
