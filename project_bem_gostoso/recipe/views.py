from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Recipe, Category
from user.models import User
from .serializers import CategorySerializer, RecipeSerializer, RecipeCreateSerializer
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, authentication_classes, permission_classes


#def manipulation_list_ingredient(ingredients_string):
#    products_format = ingredients_string.replace('[', '')
#    result_format = products_format.replace(']', '')
#    product_array = result_format.split(", ")
#    return list(map(str, product_array))

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'user']
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RecipeSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return RecipeCreateSerializer
