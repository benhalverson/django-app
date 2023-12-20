from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


@extend_schema(responses={200: CategorySerializer})
class CategoryViewSet(viewsets.ModelViewSet ):
    """
    A simple Viewset for viewing all categories.
    """
    try:
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
    except Exception as e:
        print(e)

@extend_schema(responses={200: BrandSerializer})
class BrandViewSet(viewsets.ModelViewSet):
    """
    A simple Viewset for viewing all brands.
    """
    try:
        queryset = Brand.objects.all()
        serializer_class = BrandSerializer
    except Exception as e:
        print(e) 
@extend_schema(responses={200: ProductSerializer})
class ProductViewSet(viewsets.ModelViewSet ):
    """
    A simple Viewset for viewing all products.
    """
    try:
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    except Exception as e:
        print(e)