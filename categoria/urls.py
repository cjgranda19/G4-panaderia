from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import confirm_update

router = DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]