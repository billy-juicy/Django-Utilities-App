from django.http import Http404
from .models import Service
from .models import Tariff
from .models import Invoice
from .models import Meter
from .models import Payment
from django.views.generic import ListView, DetailView


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

class TariffListView(ListView):
    model = Tariff
    template_name = 'tariff.html' # Путь к шаблону
    context_object_name = 'tariffs' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        a = self.request.user.username

        if not queryset.exists():
            raise Http404('Нет тарифов для отображения!')
        return queryset

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice.html' # Путь к шаблону
    context_object_name = 'invoices' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        a = self.request.user.username

        if not queryset.exists():
            raise Http404('Нет квитанций для отображения!')
        return queryset

class MeterListView(ListView):
    model = Meter
    template_name = 'meter.html' # Путь к шаблону
    context_object_name = 'meters' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        a = self.request.user.username

        if not queryset.exists():
            raise Http404('Нет счетчиков для отображения!')
        return queryset

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment.html' # Путь к шаблону
    context_object_name = 'payments' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        a = self.request.user.username

        if not queryset.exists():
            raise Http404('Нет платежей для отображения!')
        return queryset
