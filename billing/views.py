from django.http import Http404
from .models import Service
from django.views.generic import ListView

class ServiceListView(ListView):
    model = Service
    template_name = 'service.html' # Путь к шаблону
    context_object_name = 'services' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        a = self.request.user.username

        if not queryset.exists():
            raise Http404('Нет услуг для отображения!')
        return queryset