from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Recipe, Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

