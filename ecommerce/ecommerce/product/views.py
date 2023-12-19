from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category
from .serializers import CategorySerializer


@extend_schema(responses={200: CategorySerializer})
class CategoryViewSet(viewsets.ModelViewSet ):
    """
    A simple Viewset for viewing all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer