from django.contrib import admin

from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')

admin.site.register(Client)
