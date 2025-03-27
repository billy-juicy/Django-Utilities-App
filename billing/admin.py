from django.contrib import admin
from .models import Invoice
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    search_fields = ('name', 'unit')
    list_filter = ('name', 'unit')

admin.site.register(Service, ServiceAdmin)


