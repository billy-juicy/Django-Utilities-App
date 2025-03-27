from django.http import Http404
from .models import Client
from django.views.generic import ListView

class ClientListView(ListView):
    model = Client
    template_name = 'clients/home.html' # Путь к шаблону
    context_object_name = 'clients' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        if not queryset.exists():
            raise Http404('Нет клиентов для отображения!')
        return queryset
