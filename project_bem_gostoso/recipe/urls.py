from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet, basename="categories")
router.register("recipe", views.RecipeViewSet, basename="recipes")


urlpatterns = [
    path('', include(router.urls)),
]
