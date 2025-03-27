from django.urls import path
from .views import home
from ..practice.urls import urlpatterns

urlpatterns = [
    path('', home, name='home'), # Главная страница
]