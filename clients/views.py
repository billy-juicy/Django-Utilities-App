from django.http import Http404
from .models import Client
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Homepage(TemplateView):
    template_name = 'home.html'

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients.html' # Путь к шаблону
    context_object_name = 'clients' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        if not queryset.exists():
            raise Http404('Нет клиентов для отображения!')
        return queryset
