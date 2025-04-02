from django.urls import path
from .views import ServiceListView
from .views import TariffListView
from .views import InvoiceListView
from .views import MeterListView
from .views import PaymentListView

urlpatterns = [
    path('services', ServiceListView.as_view(), name='services-list'),
    path('tariffs', TariffListView.as_view(), name='tariffs-list'),
    path('invoices', InvoiceListView.as_view(), name='invoices-list'),
    path('meters', MeterListView.as_view(), name='meters-list'),
    path('payments', PaymentListView.as_view(), name='payments-list'),
]