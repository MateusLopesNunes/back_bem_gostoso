from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", views.UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('create', views.CreateUser.as_view()),
    path('reset_password', views.reset_password),
]
