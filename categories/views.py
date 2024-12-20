from django.shortcuts import render

# Create your views here.
from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Products
from products.serializers import ProductsSerializer
class CategoriesListView(APIView):
    def get(self, request):
        try:
            categories = Categories.objects.all()
            serializer = CategoriesSerializer(categories, many=True)
            return Response({"Categories": serializer.data})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CategoriesCreateView(APIView):
    def post(self, request):
        try:
            serializer = CategoriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CategoriesDetailView(APIView):
    def get(self, request, category_id):
        try:
            # Fetch the category by ID
            category = Categories.objects.get(id=category_id)
            
            # Serialize the category data
            category_serializer = CategoriesSerializer(category)
            
            # Fetch related products for the category
            products = Products.objects.filter(category=category)
            
            # Serialize the related products
            products_serializer = ProductsSerializer(products, many=True)
            
            # Include the serialized products in the response
            response_data = category_serializer.data
            response_data['products'] = products_serializer.data
            
            return Response(response_data)
        
        except Categories.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, category_id):
        try:
            categories = Categories.objects.get(id=category_id)
            serializer = CategoriesSerializer(categories, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Categories.DoesNotExist:
            return Response({"error": "Categories not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, category_id):
        try:
            categories = Categories.objects.get(id=category_id)
            categories.delete()
            return Response({"message": "Categories deleted successfully"})
        except Categories.DoesNotExist:
            return Response({"error": "Categories not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)