from datetime import timezone, timedelta
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import ComplaintForm
from .models import Client, Complaint
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete


class Homepage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['clients_count'] = Client.objects.count()
            context['active_complaints'] = Complaint.objects.filter(status='open').count()
            context['new_complaints'] = Complaint.objects.filter(
                status='open',
                date_filed__gte=timezone.now() - timedelta(days=7)
            ).count()
            context['last_complaints'] = Complaint.objects.select_related('client').order_by('-date_filed')[:5]
            return context

class ClientListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Client
    template_name = 'clients.html' # Путь к шаблону
    context_object_name = 'clients' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        if not queryset.exists():
            raise Http404('Нет клиентов для отображения!')
        return queryset

from rest_framework import viewsets, permissions, pagination
from rest_framework.exceptions import NotFound
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination  # Пагинация как в ListView
    pagination_class.page_size = 3

    def get_queryset(self):
        queryset = Client.objects.all()
        if not queryset.exists():
            raise NotFound(detail="Нет клиентов для отображения!")
        return queryset

class AddComplaintFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
     model = Complaint
     form = ComplaintForm
     success_url = reverse_lazy('homepage')
     fields = ['client', 'description', 'status']
     template_name = 'complaint_add_form.html'
     success_url = reverse_lazy("complaints-success")
     success_message = "Ваша жалоба успешно зарегистрирована!"

class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Client.objects.none()

        qs = Client.objects.all()

        if self.q:
            qs = qs.filter(Q(first_name__contains=self.q) | Q(last_name__contains=self.q))

        return qs

