from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Recipe, Category, Ingredient
from user.models import User
from .serializers import CategorySerializer, RecipeSerializer, RecipeCreateSerializer
from rest_framework.response import Response

def manipulation_list_ingredient(ingredients_string):
    products_format = ingredients_string.replace('[', '')
    result_format = products_format.replace(']', '')
    product_array = result_format.split(", ")
    return list(map(str, product_array))

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RecipeSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return RecipeCreateSerializer

    def create(self, request):
        req = request.data
        category = Category.objects.filter(id=req['category'])
        user = User.objects.filter(id=req['user'])

        ingredients = manipulation_list_ingredient(req['ingredient'])

        recipe = Recipe(
            title = req['title'],
            number_of_portion = req['number_of_portion'],
            preparation_method = req['preparation_method'],
            preparation_time = req['preparation_time'],
            recipe_image = req['recipe_image'],
            category = category[0],
            user = user[0],
        )
        recipe.ingredients.append(ingredients)
        recipe.save()

        return Response({'msg': ingredients})
        #return Response({'msg': 'Receita cadastrada com sucesso'})