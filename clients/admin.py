from django.contrib import admin

from .models import Client
from .models import Complaint
from .models import Property

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')

admin.site.register(Client)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_filed', 'description', 'status')
    search_fields = ('client__last_name', 'date_filed', 'description', 'status')
    list_filter = ('client__last_name', 'date_filed', 'description', 'status')

admin.site.register(Complaint)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'address', 'type', 'area')
    search_fields = ('owner', 'address', 'type', 'area')
    list_filter = ('owner', 'address', 'type', 'area')

admin.site.register(Property)