from django.shortcuts import render
from django.http import Http404
from .models import Client

def home(request):
    clients = Client.objects.all() # Получаем всех клиентов

    if not clients: # Исключение
        raise Http404('Нет клиентов для отображения!')

    return render(request, 'clients/home.html', {'clients': clients}) # Передаем всех клиентов в шаблон