from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category/')

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    number_of_portion = models.CharField(max_length=100)
    ingredient_id = models.CharField(max_length=100)
    preparation_method = models.CharField(max_length=100)
    preparation_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    perfil_image = models.ImageField(upload_to='user/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

