from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", views.CategoryViewSet, basename="categories")

urlpatterns = [
    path('category/', include(router.urls)),
]
