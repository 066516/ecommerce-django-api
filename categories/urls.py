#Categories/urls.py
from django.urls import path
from .views import  CategoriesListView,CategoriesCreateView,CategoriesDetailView

urlpatterns = [
    path('categories', CategoriesCreateView.as_view(), name='create_Categories'),
    path('categories/list', CategoriesListView.as_view(), name='Categories_list'),
    path('categories/<int:category_id>', CategoriesDetailView.as_view(), name='Categories_detail'),
]