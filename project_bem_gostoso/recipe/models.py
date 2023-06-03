from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category/')


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    number_of_portion = models.CharField(max_length=100)
    preparation_method = models.CharField(max_length=100)
    preparation_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    recipe_image = models.ImageField(upload_to='recipe/', blank=True, null=True, default='default/índice.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    ingredients = []

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    #recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)

class Ingredient_recipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=False)
