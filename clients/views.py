from django.shortcuts import render
from .models import Client

def home(request):
    clients = Client.objects.all() # Получаем всех клиентов
    return render(request, 'clients/home.html', {'clients': clients}) # Передаем всех клиентов в шаблон