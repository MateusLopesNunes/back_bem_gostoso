from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet, basename="categories")
router.register("recipe", views.RecipeViewSet, basename="recipes")


urlpatterns = [
    path('', include(router.urls)),
    path('create/recipe', views.create_recipe),
    path('list/recipe/', views.List_recipe.as_view()),
    path('get/recipe/<int:pk>', views.Get_recipe.as_view()),
    path('delete/recipe/<int:pk>', views.Delete_recipe.as_view()),
]
