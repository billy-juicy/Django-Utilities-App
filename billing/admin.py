from django.contrib import admin
from .models import Invoice
from .models import Service
from .models import Tariff
from .models import Debt
from .models import Payment
from .models import Meter
from .models import MeterReading

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    search_fields = ('name', 'unit')
    list_filter = ('name', 'unit')

admin.site.register(Service, ServiceAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_issued', 'due_date', 'total_amount', 'status')
    search_fields = ('client', 'date_issued', 'due_date', 'total_amount', 'status')
    list_filter = ('client', 'date_issued', 'due_date', 'total_amount', 'status')

admin.site.register(Invoice, InvoiceAdmin)

class TariffAdmin(admin.ModelAdmin):
    list_display = ('service', 'rate', 'start_date', 'end_date')
    search_fields = ('service', 'rate', 'start_date', 'end_date')
    list_filter = ('service', 'rate', 'start_date', 'end_date')

admin.site.register(Tariff, TariffAdmin)

class DebtAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'due_date', 'status')
    search_fields = ('client', 'amount', 'due_date', 'status')
    list_filter = ('client', 'amount', 'due_date', 'status')

admin.site.register(Debt, DebtAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'date_paid', 'amount', 'method')
    search_fields = ('invoice', 'date_paid', 'amount', 'method')
    list_filter = ('invoice', 'date_paid', 'amount', 'method')

admin.site.register(Payment, PaymentAdmin)

class MeterAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'meter_number', 'installation_date')
    search_fields = ('client', 'service', 'meter_number', 'installation_date')
    list_filter = ('client', 'service', 'meter_number', 'installation_date')

admin.site.register(Meter, MeterAdmin)

class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('meter', 'reading_date', 'value')
    search_fields = ('meter', 'reading_date', 'value')
    list_filter = ('meter', 'reading_date', 'value')

admin.site.register(MeterReading, MeterReadingAdmin)