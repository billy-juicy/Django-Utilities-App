from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse, reverse_lazy
from .models import Client, Complaint
from django.views.generic import ListView, TemplateView, CreateView
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

class AddComplaintFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
     model = Complaint
     fields = ['client', 'description', 'status']
     template_name = 'complaint_add_form.html'
     success_url = reverse_lazy("complaints-success")
     success_message = "Ваша жалоба успешно зарегистрирована!"




