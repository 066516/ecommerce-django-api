#products/urls.py
from django.urls import path
from .views import ProductsListView,ProductsCreateView,ProductsDetail
urlpatterns = [
    path('products/list', ProductsListView.as_view(), name='products_list'),
    path('products',ProductsCreateView.as_view(),name='create_product'),
    path('products/<int:product_id>', ProductsDetail.as_view(), name='products_detail'),
]