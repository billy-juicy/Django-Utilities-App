from django.http import Http404
from .models import Service, Debt, MeterReading
from .models import Tariff
from .models import Invoice
from .models import Meter
from .models import Payment
from .forms import CalculateForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calculate_form'] = CalculateForm()
        return context

class InvoiceListView(ListView):
    paginate_by = 3 # Пагинация
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
    paginate_by = 3 # Пагинация
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
    paginate_by = 3 # Пагинация
    model = Payment
    template_name = 'payment.html' # Путь к шаблону
    context_object_name = 'payments' # Название списка в шаблоне

    def get_queryset(self):
        queryset = super().get_queryset()

        a = self.request.user.username

        if not queryset.exists():
            raise Http404('Нет платежей для отображения!')
        return queryset

class DebtDetailView(DetailView):
    model = Debt
    template_name = 'debt.html'
    context_object_name = 'debt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MeterReadingListView(ListView):
    paginate_by = 3 # Пагинация
    model = MeterReading
    template_name = 'meter_reading.html'
    context_object_name = 'meter_readings'

    def get_queryset(self):
        queryset = super().get_queryset()

        if not queryset.exists():
            raise Http404('Нет показателей счетчиков для отображения!')
        return queryset