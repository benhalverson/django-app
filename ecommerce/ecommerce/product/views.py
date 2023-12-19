from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet ):
    """
    A simple Viewset for viewing all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer