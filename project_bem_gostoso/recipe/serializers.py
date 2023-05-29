from .models import Category, Recipe
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 5

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id','title', 'number_of_portion', 'preparation_method', 'preparation_time', 'created_at', 'updated_at', 'recipe_image', 'category', 'user', 'ingredients']
        depth = 5

class RecipeCreateSerializer(serializers.ModelSerializer):
    #ingredient = serializers.ListField(child=serializers.CharField(max_length=100))
    class Meta:
        model = Recipe
        exclude = ['created_at', 'updated_at']
